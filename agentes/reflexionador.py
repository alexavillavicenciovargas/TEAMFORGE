"""Persona 3 — Actualiza perfiles y extrae hipótesis."""
from config import RASGOS
def actualizar_perfiles(personas,resultados,alpha=.3):
 ix={p["id"]:p for p in personas}
 for res in resultados:
  for pid,fb in res["feedback"].items():
   if pid not in ix: continue
   for x in RASGOS:
    if x in fb: ix[pid]["estimado"][x]=round((1-alpha)*ix[pid]["estimado"][x]+alpha*fb[x],3)
def sacar_lecciones(historial,personas,tipo):
 ix={p["id"]:p for p in personas}; out=[]
 for x in RASGOS:
  for q in range(4):
   yes=[]; no=[]
   for h in historial:
    e=[ix[z] for z in h["miembros"] if z in ix]; n=sum(p["estimado"][x]>=4 for p in e)
    (yes if n>=q else no).append(h["score"])
   if len(yes)>=3 and len(no)>=3:
    a=sum(yes)/len(yes); b=sum(no)/len(no)
    if abs(a-b)>8: out.append({"tipo_proyecto":tipo,"rasgo":x,"umbral":4,"operador":"max","cantidad":q,"texto":f"Hipótesis: {q} o más con {x} >= 4; delta observado {a-b:.1f}.","evidencia":{"media_cumple":a,"media_no_cumple":b,"n_cumple":len(yes),"n_no_cumple":len(no)}})
 return out