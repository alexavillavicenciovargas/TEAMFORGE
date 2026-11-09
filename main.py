"""Persona 1 — Demo reproducible y orquestación."""
import argparse,json,copy
from pathlib import Path
from config import *
from personas import generar_personas,guardar
from agentes.constructor import armar_equipos
from agentes.evaluador import evaluar
from agentes.reflexionador import actualizar_perfiles,sacar_lecciones
from agentes.curador import Biblioteca
from almacenamiento import Almacenamiento
def error(ps): return round(sum(abs(p["estimado"][r]-p["real"][r]) for p in ps for r in RASGOS)/(len(ps)*len(RASGOS)),3)
def demo(modo="determinista",n=N_PERSONAS,semilla=SEMILLA):
 p=generar_personas(n,semilla); guardar(p); db=Almacenamiento(); db.registrar_lote(f"lote-{semilla}-{n}",semilla,n)
 con=copy.deepcopy(p); sin=copy.deepcopy(p); lib=Biblioteca(); cm=[]; sm=[]
 for i in range(RONDAS):
  t=TIPOS_PROYECTO[i%3]; eq=armar_equipos(con,t,lib.relevantes(t),semilla=semilla+i); rs=evaluar(eq,t,i+1); actualizar_perfiles(con,rs)
  for l in sacar_lecciones(rs,con,t): lib.agregar(l)
  cm.append({"ronda":i+1,"tipo":t,"score_promedio":round(sum(x["score"] for x in rs)/len(rs),3),"error_perfiles":error(con),"lecciones":len(lib.lecciones)})
  eq0=armar_equipos(sin,t,[],semilla=semilla+i); r0=evaluar(eq0,t,i+1)
  sm.append({"ronda":i+1,"tipo":t,"score_promedio":round(sum(x["score"] for x in r0)/len(r0),3),"error_perfiles":error(sin),"lecciones":0})
 Path("resultados").mkdir(exist_ok=True)
 data={"con_memoria":cm,"sin_memoria":sm,"personas":con,"reglas_ocultas":["Efectos sintéticos específicos por proyecto","Ruido reproducible"]}
 Path("resultados/metricas.json").write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding="utf-8")
 ev={"schema_version":"1.0","modo":modo,"estrategia_vigente":{"id":"v1","pesos":{"cumplimiento_lecciones":.7,"balance":.3},"presupuesto_busqueda":300,"lecciones":[],"schema_version":"1.0"},"candidatos":[],"nota":"No se afirma mejora autónoma sin validación."}
 if modo=="api":
  from llm import analizar_con_subagentes_sync
  contexto={"muestras":cm,"perfiles_observables":[{k:v for k,v in x.items() if k!="real"} for x in con]}
  ev["subagentes"]=analizar_con_subagentes_sync(contexto)
 Path("resultados/evolucion.json").write_text(json.dumps(ev,indent=2,ensure_ascii=False),encoding="utf-8")
 db.registrar_experimento("demo-inicial",modo,{"semilla":semilla,"rondas":RONDAS})
 print("Demo lista: resultados/metricas.json y resultados/evolucion.json"); return data
if __name__=="__main__":
 a=argparse.ArgumentParser(); s=a.add_subparsers(dest="cmd",required=True); d=s.add_parser("demo"); d.add_argument("--mode",choices=["determinista","api"],default="determinista"); d.add_argument("--personas",type=int,default=N_PERSONAS); d.add_argument("--seed",type=int,default=SEMILLA); x=s.add_parser("evaluar"); z=a.parse_args()
 if z.cmd=="demo": demo(z.mode,z.personas,z.seed)
 else: print("Consulta docs/evaluacion.md")