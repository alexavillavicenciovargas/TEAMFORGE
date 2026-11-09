"""Persona 2 — Evaluador sintético externo fijo."""
import random
from config import RASGOS
EFECTOS={"creativo":{"creatividad":5.0,"extroversion":1.2,"organizacion":.5},"tecnico":{"organizacion":4.0,"cumplimiento":3.0,"creatividad":1.0},"entrega_rapida":{"cumplimiento":4.5,"organizacion":3.0,"liderazgo":1.5}}
def simular(equipo,tipo,semilla):
 r=random.Random(semilla)
 if tipo not in EFECTOS: raise ValueError(tipo)
 medias={x:sum(p["real"][x] for p in equipo)/len(equipo) for x in RASGOS}
 score=48+sum(EFECTOS[tipo].get(x,0)*(medias[x]-3) for x in RASGOS)+1.8*(max(medias.values())-min(medias.values()))+r.uniform(-2,2)
 feedback={p["id"]:{x:round(max(1,min(5,p["real"][x]+r.uniform(-.45,.45))),3) for x in RASGOS} for p in equipo}
 return {"score":round(max(0,min(100,score)),3),"feedback":feedback}