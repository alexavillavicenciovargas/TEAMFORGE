"""Persona 2 — Perfiles sintéticos. Nunca representan personas reales."""
import json, random
from pathlib import Path
from config import RASGOS, N_PERSONAS

def generar_personas(n=N_PERSONAS, semilla=42):
    rng = random.Random(semilla)
    personas = []
    for i in range(n):
        real = {r: rng.randint(1, 5) for r in RASGOS}
        declarado = dict(real)
        grupo = i % 6
        if grupo in (0, 1):
            r = rng.choice(RASGOS); declarado[r] = min(5, real[r] + rng.randint(1, 2))
        elif grupo == 2:
            r = rng.choice(RASGOS); declarado[r] = max(1, real[r] - rng.randint(1, 2))
        personas.append({"id": f"P{i+1:03}", "nombre": f"Perfil {i+1:03}",
                         "declarado": declarado, "real": real, "estimado": dict(declarado)})
    return personas

def guardar(personas, ruta="datos/personas.json"):
    p = Path(ruta); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(personas, indent=2, ensure_ascii=False), encoding="utf-8")

def cargar(ruta="datos/personas.json"):
    return json.loads(Path(ruta).read_text(encoding="utf-8"))
