"""Persona 3 — Propone cambios acotados y casos declarativos."""
import copy, uuid
def construir_candidatos(estrategia, lecciones, max_candidatos=3):
    candidatos=[]
    for i, leccion in enumerate(lecciones[:max_candidatos]):
        nueva=copy.deepcopy(estrategia)
        nueva["id"]=f"cand-{uuid.uuid4().hex[:8]}"
        nueva["version_padre"]=estrategia["id"]
        nueva["lecciones"]=list(estrategia.get("lecciones",[]))+[leccion]
        candidatos.append({"id":nueva["id"],"estrategia":nueva,
                           "motivacion":leccion.get("texto","Regla propuesta"),
                           "evidencia_ids":[leccion.get("id","evidencia-descubrimiento")]})
    return candidatos

def caso_regresion(fallo):
    return {"id":f"reg-{uuid.uuid4().hex[:8]}","entrada":fallo,
            "condicion":{"tipo":"equipo_sin_duplicados"},
            "evidencia":{"origen":"fallo_observado" if fallo else "mecanismo"},
            "resultado_esperado":True,"schema_version":"1.0"}
