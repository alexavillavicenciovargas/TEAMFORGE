"""Persona 3 — Builder limitado a configuraciones."""
import copy,uuid
def construir_candidatos(estrategia,lecciones,max_candidatos=3):
 out=[]
 for l in lecciones[:max_candidatos]:
  e=copy.deepcopy(estrategia); e["id"]="cand-"+uuid.uuid4().hex[:8]; e["version_padre"]=estrategia["id"]; e["lecciones"]=list(e.get("lecciones",[]))+[l]
  out.append({"id":e["id"],"estrategia":e,"motivacion":l.get("texto","Hipótesis"),"evidencia_ids":[l.get("id","descubrimiento")]})
 return out