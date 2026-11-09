"""Persona 1 — Valida y conserva versiones inmutables."""
from contratos import validar_estrategia
from benchmark import evaluar_estrategia

def comparar(personas, vigente, candidato):
    validar_estrategia(candidato["estrategia"])
    antes=evaluar_estrategia(personas,vigente)
    despues=evaluar_estrategia(personas,candidato["estrategia"])
    dif={t:round(despues["por_tipo"][t]["media"]-antes["por_tipo"][t]["media"],3)
         for t in antes["por_tipo"]}
    aceptada=(despues["media"]-antes["media"] >= 2 and all(v >= -2 for v in dif.values()))
    return {"aceptada":aceptada,"antes":antes,"despues":despues,"diferencias":dif,
            "motivo":"Mejora >=2 y ningún tipo cae más de 2." if aceptada else
                     "No cumple umbrales fijos; se conserva la estrategia vigente."}
