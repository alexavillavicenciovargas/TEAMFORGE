"""Persona 3 — Actualiza estimaciones y extrae hipótesis de los resultados."""
from config import RASGOS
def actualizar_perfiles(personas, resultados, alpha=0.3):
    por_id = {p["id"]: p for p in personas}
    for resultado in resultados:
        for pid, feedback in resultado["feedback"].items():
            if pid in por_id:
                for rasgo in RASGOS:
                    if rasgo not in feedback:
                        continue
                    p = por_id[pid]
                    p["estimado"][rasgo] = round((1-alpha)*p["estimado"][rasgo] + alpha*feedback[rasgo], 3)

def sacar_lecciones(historial, personas, tipo):
    por_id = {p["id"]: p for p in personas}
    propuestas = []
    for rasgo in RASGOS:
        for umbral in (4,):
            for cantidad in range(4):
                si, no = [], []
                for h in historial:
                    equipo = [por_id[x] for x in h["miembros"] if x in por_id]
                    n = sum(p["estimado"][rasgo] >= umbral for p in equipo)
                    (si if n >= cantidad else no).append(h["score"])
                if len(si) >= 3 and len(no) >= 3:
                    delta = sum(si)/len(si) - sum(no)/len(no)
                    if abs(delta) > 8:
                        propuestas.append({"tipo_proyecto": tipo, "rasgo": rasgo, "umbral": umbral,
                            "operador": "max", "cantidad": cantidad,
                            "texto": f"Hipótesis: al menos {cantidad} integrantes con {rasgo} >= {umbral}; diferencia observada {delta:.1f} puntos.",
                            "evidencia": {"media_cumple": round(sum(si)/len(si), 2),
                                          "media_no_cumple": round(sum(no)/len(no), 2),
                                          "n_cumple": len(si), "n_no_cumple": len(no)}})
    return propuestas
