"""Persona 3 — Adaptador OpenAI Agents SDK opcional; no recibe perfiles reales."""
import os, json, asyncio
def api_disponible():
    return bool(os.getenv("OPENAI_API_KEY"))

async def _run_specialist(name, instructions, payload, model):
    from agents import Agent, Runner
    agent=Agent(name=name,instructions=instructions,model=model)
    result=await Runner.run(agent, json.dumps(payload,ensure_ascii=False))
    return result.final_output

async def analizar_con_subagentes(payload, model=None):
    """Orquestación explícita: analista -> estratega -> revisor. Cada etapa es un Agent real."""
    if not api_disponible(): raise RuntimeError("Falta OPENAI_API_KEY")
    model=model or os.getenv("OPENAI_MODEL","gpt-5.5")
    analisis=await _run_specialist("Analista de perfiles",
        "Analiza únicamente perfiles observables y métricas agregadas. Nunca solicites ni infieras perfiles reales. Devuelve hallazgos con evidencia y limitaciones.",payload,model)
    propuesta=await _run_specialist("Estratega de equipos",
        "Propón hasta 3 cambios declarativos a la configuración. No cambies simulador, métrica, semillas ni pruebas reservadas. Devuelve JSON si es posible.",{"hallazgos":analisis,"contexto":payload},model)
    revision=await _run_specialist("Revisor independiente",
        "Audita la propuesta contra las restricciones. Identifica riesgos, datos no sustentados y pruebas necesarias. No afirmes que la mejora está demostrada.",{"analisis":analisis,"propuesta":propuesta},model)
    return {"modo":"openai_agents_sdk","analisis":analisis,"propuesta":propuesta,"revision":revision}

def analizar_con_subagentes_sync(payload):
    return asyncio.run(analizar_con_subagentes(payload))
