"""Persona 1 — Ejecuta equipos en el simulador y devuelve evidencia."""
from simulador import simular
def evaluar(equipos, tipo, ronda):
    resultados = []
    for i, equipo in enumerate(equipos):
        r = simular(equipo, tipo, semilla=1000*ronda+i)
        resultados.append({"miembros": [p["id"] for p in equipo], "tipo": tipo,
                           "ronda": ronda, "score": r["score"], "feedback": r["feedback"]})
    return resultados
