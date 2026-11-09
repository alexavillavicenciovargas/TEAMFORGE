"""Persona 3 — OpenAI Agents SDK. Nunca pasa perfiles reales a los prompts."""
import os,asyncio,json
def api_disponible(): return bool(os.getenv("OPENAI_API_KEY"))
async def _run(name,instructions,payload,model):
 from agents import Agent,Runner
 result=await Runner.run(Agent(name=name,instructions=instructions,model=model),json.dumps(payload,ensure_ascii=False))
 return result.final_output
async def analizar_con_subagentes(payload,model=None):
 if not api_disponible(): raise RuntimeError("Falta OPENAI_API_KEY")
 model=model or os.getenv("OPENAI_MODEL","gpt-5.5")
 a=await _run("Analista de perfiles","Analiza solo perfiles observables y métricas agregadas. Devuelve hallazgos con evidencia y limitaciones.",payload,model)
 b=await _run("Estratega de equipos","Propón hasta 3 cambios declarativos. No cambies simulador, métrica, semillas ni pruebas reservadas.",{"hallazgos":a,"contexto":payload},model)
 c=await _run("Revisor independiente","Audita la propuesta; enumera evidencia faltante, riesgos y pruebas. No afirmes mejora demostrada.",{"analisis":a,"propuesta":b},model)
 return {"modo":"openai_agents_sdk","analisis":a,"propuesta":b,"revision":c}
def analizar_con_subagentes_sync(p): return asyncio.run(analizar_con_subagentes(p))