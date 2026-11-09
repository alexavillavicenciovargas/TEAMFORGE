"""Persona 1 — Evaluación de equipos."""
from simulador import simular
def evaluar(equipos,tipo,ronda):
 out=[]
 for i,e in enumerate(equipos):
  x=simular(e,tipo,1000*ronda+i); out.append({"miembros":[p["id"] for p in e],"tipo":tipo,"ronda":ronda,"score":x["score"],"feedback":x["feedback"]})
 return out