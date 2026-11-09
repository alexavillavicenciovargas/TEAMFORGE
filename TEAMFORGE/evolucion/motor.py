"""Persona 1 — Selección explícita de equipos según configuración versionada."""
from agentes.constructor import armar_equipos
def seleccionar(personas, tipo, lecciones, estrategia, semilla=0):
    return armar_equipos(personas,tipo,lecciones,semilla=semilla)
