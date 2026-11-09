"""Persona 1 — Constructor con acceso solo a estimaciones."""
import random
from config import RASGOS,TAM_EQUIPO
def cumple(e,l):
 n=sum((p["estimado"][l["rasgo"]]>=l["umbral"] if l["operador"]=="max" else p["estimado"][l["rasgo"]]<=l["umbral"]) for p in e)
 return n>=l["cantidad"]
def armar_equipos(personas,tipo,lecciones,tam=TAM_EQUIPO,semilla=0):
 if tam<=0 or len(personas)%tam: raise ValueError(f"Población debe ser divisible entre {tam}; recibidos: {len(personas)}")
 r=random.Random(semilla)
 if not lecciones:
  p=list(personas); r.shuffle(p); return [p[i:i+tam] for i in range(0,len(p),tam)]
 best=None; keybest=None
 for _ in range(300):
  p=list(personas); r.shuffle(p); eq=[p[i:i+tam] for i in range(0,len(p),tam)]
  v=sum(not cumple(e,l) for e in eq for l in lecciones if l["tipo_proyecto"] in (tipo,"todos"))
  b=sum(max(sum(p["estimado"][x] for p in e)/tam for x in RASGOS)-min(sum(p["estimado"][x] for p in e)/tam for x in RASGOS) for e in eq)
  k=(v,b)
  if keybest is None or k<keybest: best,keybest=eq,k
 return best