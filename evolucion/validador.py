"""Persona 1 — Validación independiente."""
from contratos import validar_estrategia
from benchmark import evaluar_estrategia
def comparar(personas,vigente,candidato):
 validar_estrategia(candidato["estrategia"]); a=evaluar_estrategia(personas,vigente); b=evaluar_estrategia(personas,candidato["estrategia"])
 d={t:round(b["por_tipo"][t]["media"]-a["por_tipo"][t]["media"],3) for t in a["por_tipo"]}
 ok=b["media"]-a["media"]>=2 and all(x>=-2 for x in d.values())
 return {"aceptada":ok,"antes":a,"despues":b,"diferencias":d,"motivo":"Umbrales cumplidos" if ok else "No cumple umbrales; conservar vigente"}