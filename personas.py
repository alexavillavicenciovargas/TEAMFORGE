"""Persona 2 — Perfiles sintéticos, nunca personas reales."""
import json, random
from pathlib import Path
from config import RASGOS,N_PERSONAS
def generar_personas(n=N_PERSONAS,semilla=42):
 r=random.Random(semilla); out=[]
 for i in range(n):
  real={x:r.randint(1,5) for x in RASGOS}; declarado=dict(real); grupo=i%6
  if grupo in (0,1):
   x=r.choice(RASGOS); declarado[x]=min(5,real[x]+r.randint(1,2))
  elif grupo==2:
   x=r.choice(RASGOS); declarado[x]=max(1,real[x]-r.randint(1,2))
  out.append({"id":f"P{i+1:03}","nombre":f"Perfil {i+1:03}","declarado":declarado,"real":real,"estimado":dict(declarado)})
 return out
def guardar(personas,ruta="datos/personas.json"):
 p=Path(ruta); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(personas,indent=2,ensure_ascii=False),encoding="utf-8")
def cargar(ruta="datos/personas.json"): return json.loads(Path(ruta).read_text(encoding="utf-8"))