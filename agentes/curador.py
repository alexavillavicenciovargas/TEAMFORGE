"""Persona 3 — Biblioteca JSON de lecciones."""
import json
from pathlib import Path
class Biblioteca:
 def __init__(self,ruta="biblioteca/lecciones.json"):
  self.ruta=Path(ruta); self.lecciones=json.loads(self.ruta.read_text(encoding="utf-8")) if self.ruta.exists() else []
 def agregar(self,l):
  keys=("tipo_proyecto","rasgo","operador","umbral","cantidad"); ident=tuple(l[k] for k in keys)
  for old in self.lecciones:
   if tuple(old[k] for k in keys)==ident: return old,False
  x={"id":f"L{len(self.lecciones)+1:04}",**{k:v for k,v in l.items() if k!="evidencia"},"veces_vista":0,"veces_aplicada":0,"veces_ayudo":0}
  self.lecciones.append(x); self.guardar(); return x,True
 def relevantes(self,t): return [x for x in self.lecciones if x["tipo_proyecto"] in (t,"todos")]
 def registrar_uso(self,lecciones,resultados):
  for x in lecciones: x["veces_vista"]+=1; x["veces_aplicada"]+=1
 def podar(self):
  self.lecciones=[x for x in self.lecciones if not(x["veces_aplicada"]>=3 and x["veces_ayudo"]==0)]; self.guardar()
 def guardar(self):
  self.ruta.parent.mkdir(parents=True,exist_ok=True); self.ruta.write_text(json.dumps(self.lecciones,indent=2,ensure_ascii=False),encoding="utf-8")