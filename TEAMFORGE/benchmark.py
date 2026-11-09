"""Persona 2 — Evaluador fijo e independiente de la estrategia."""
from config import TIPOS_PROYECTO
from agentes.constructor import armar_equipos
from simulador import simular

def evaluar_estrategia(personas, estrategia, semillas=range(5)):
    por_tipo={}
    for tipo in TIPOS_PROYECTO:
        scores=[]
        for seed in semillas:
            equipos=armar_equipos(personas,tipo,estrategia.get("lecciones",[]),semilla=seed)
            # La comparación recibe la misma población y semilla; el simulador no cambia.
            scores.extend(simular(eq,tipo,semilla=seed*100+i)["score"] for i,eq in enumerate(equipos))
        por_tipo[tipo]={"media":round(sum(scores)/len(scores),3),"n":len(scores),
                        "min":round(min(scores),3),"max":round(max(scores),3)}
    return {"por_tipo":por_tipo,"media":round(sum(x["media"] for x in por_tipo.values())/len(por_tipo),3)}
