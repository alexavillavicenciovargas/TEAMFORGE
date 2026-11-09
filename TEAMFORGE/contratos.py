"""Persona 1 — Contratos versionados para estrategias, propuestas, casos y decisiones."""
from dataclasses import dataclass, asdict
from typing import Any
SCHEMA_VERSION = "1.0"
@dataclass
class Estrategia:
    id: str
    version_padre: str | None
    pesos: dict
    presupuesto_busqueda: int
    lecciones: list
    schema_version: str = SCHEMA_VERSION
@dataclass
class Propuesta:
    id: str
    estrategia: dict
    motivacion: str
    evidencia_ids: list
    schema_version: str = SCHEMA_VERSION
@dataclass
class CasoPrueba:
    id: str
    entrada: dict
    condicion: dict
    evidencia: dict
    resultado_esperado: bool
    schema_version: str = SCHEMA_VERSION
@dataclass
class Decision:
    id: str
    candidato_id: str
    aceptada: bool
    motivo: str
    metricas: dict
    schema_version: str = SCHEMA_VERSION

def validar_estrategia(e):
    if e.get("schema_version") != SCHEMA_VERSION: raise ValueError("Versión de esquema incompatible")
    pesos=e.get("pesos", {})
    if set(pesos) != {"cumplimiento_lecciones", "balance"}: raise ValueError("Pesos no permitidos")
    if any(not isinstance(v,(int,float)) or v < 0 for v in pesos.values()): raise ValueError("Pesos deben ser no negativos")
    if abs(sum(pesos.values())-1) > 1e-8: raise ValueError("Los pesos deben sumar 1")
    if not 1 <= e.get("presupuesto_busqueda",0) <= 300: raise ValueError("Presupuesto fuera de rango")
    return True
