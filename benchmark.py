"""Persona 2 — Evaluador fijo para comparaciones futuras."""
from config import TIPOS_PROYECTO
from agentes.constructor import armar_equipos
from simulador import simular
def evaluar_estrategia(personas,estrategia,semillas=range(5)):
 res={}
 for t in TIPOS_PROYECTO:
  scores=[]
  for s in semillas:
   eq=armar_equipos(personas,t,estrategia.get("lecciones",[]),semilla=s)
   scores += [simular(e,t,s*100+i)["score"] for i,e in enumerate(eq)]
  res[t]={"media":round(sum(scores)/len(scores),3),"n":len(scores),"min":min(scores),"max":max(scores)}
 return {"por_tipo":res,"media":round(sum(x["media"] for x in res.values())/len(res),3)}