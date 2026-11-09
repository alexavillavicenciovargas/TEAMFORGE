"""Persona 3 — Biblioteca persistente de lecciones."""
import json
from pathlib import Path
class Biblioteca:
    def __init__(self, ruta="biblioteca/lecciones.json"):
        self.ruta = Path(ruta); self.lecciones = []
        if self.ruta.exists(): self.lecciones = json.loads(self.ruta.read_text(encoding="utf-8"))
    def agregar(self, leccion):
        key = tuple(leccion[k] for k in ("tipo_proyecto","rasgo","operador","umbral","cantidad"))
        for old in self.lecciones:
            if tuple(old[k] for k in ("tipo_proyecto","rasgo","operador","umbral","cantidad")) == key:
                return old, False
        item = {"id": f"L{len(self.lecciones)+1:04}", **{k:v for k,v in leccion.items() if k != "evidencia"},
                "veces_vista": 0, "veces_aplicada": 0, "veces_ayudo": 0}
        self.lecciones.append(item); self.guardar(); return item, True
    def relevantes(self, tipo):
        return [l for l in self.lecciones if l["tipo_proyecto"] in (tipo, "todos")]
    def registrar_uso(self, lecciones, resultados):
        for l in lecciones:
            l["veces_vista"] += 1; l["veces_aplicada"] += 1
    def podar(self):
        self.lecciones = [l for l in self.lecciones if not (l["veces_aplicada"] >= 3 and l["veces_ayudo"] == 0)]
        self.guardar()
    def guardar(self):
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self.ruta.write_text(json.dumps(self.lecciones, indent=2, ensure_ascii=False), encoding="utf-8")
