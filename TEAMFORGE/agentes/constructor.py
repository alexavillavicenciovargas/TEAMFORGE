"""Persona 1 — Formación de equipos sin acceso a perfiles reales."""
import random
from config import TAM_EQUIPO, RASGOS

def cumple(equipo, leccion):
    cantidad = sum(1 for p in equipo if (
        p["estimado"][leccion["rasgo"]] >= leccion["umbral"]
        if leccion["operador"] == "max" else p["estimado"][leccion["rasgo"]] <= leccion["umbral"]))
    return cantidad >= leccion["cantidad"]

def armar_equipos(personas, tipo, lecciones, tam=TAM_EQUIPO, semilla=0):
    if tam <= 0 or len(personas) % tam:
        raise ValueError(f"Se requieren grupos divisibles entre {tam}; recibidos: {len(personas)}")
    rng = random.Random(semilla)
    if not lecciones:
        pool = list(personas); rng.shuffle(pool)
        return [pool[i:i+tam] for i in range(0, len(pool), tam)]
    best, best_key = None, None
    for _ in range(300):
        pool = list(personas); rng.shuffle(pool)
        equipos = [pool[i:i+tam] for i in range(0, len(pool), tam)]
        violations = sum(not cumple(eq, l) for eq in equipos for l in lecciones if l["tipo_proyecto"] in (tipo, "todos"))
        balance = sum((max(sum(p["estimado"][r] for p in eq)/tam for r in RASGOS) -
                       min(sum(p["estimado"][r] for p in eq)/tam for r in RASGOS)) for eq in equipos)
        key = (violations, round(balance, 6))
        if best_key is None or key < best_key: best, best_key = equipos, key
    return best
