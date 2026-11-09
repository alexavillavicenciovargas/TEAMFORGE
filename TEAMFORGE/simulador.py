"""Persona 2 — Simulador externo fijo; usa perfil real solo dentro del simulador."""
import random
from config import RASGOS

EFECTOS = {
    "creativo": {"creatividad": 5.0, "extroversion": 1.2, "organizacion": 0.5},
    "tecnico": {"organizacion": 4.0, "cumplimiento": 3.0, "creatividad": 1.0},
    "entrega_rapida": {"cumplimiento": 4.5, "organizacion": 3.0, "liderazgo": 1.5},
}

def simular(equipo, tipo, semilla):
    rng = random.Random(semilla)
    if tipo not in EFECTOS: raise ValueError(f"Tipo desconocido: {tipo}")
    medias = {r: sum(p["real"][r] for p in equipo)/len(equipo) for r in RASGOS}
    score = 48 + sum(EFECTOS[tipo].get(r, 0) * (medias[r]-3) for r in RASGOS)
    # Complementariedad y ruido reproducible; fórmula congelada para comparar candidatos.
    score += 1.8 * (max(medias.values()) - min(medias.values()))
    score += rng.uniform(-2.0, 2.0)
    score = round(max(0.0, min(100.0, score)), 3)
    feedback = {p["id"]: {r: round(max(1, min(5, p["real"][r] + rng.uniform(-0.45, 0.45))), 3)
                          for r in RASGOS} for p in equipo}
    return {"score": score, "feedback": feedback}
