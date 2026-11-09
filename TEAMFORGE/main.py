"""Persona 1 — CLI y orquestación de la demo."""
import argparse, json, copy
from pathlib import Path
from config import *
from personas import generar_personas, guardar
from agentes.constructor import armar_equipos
from agentes.evaluador import evaluar
from agentes.reflexionador import actualizar_perfiles, sacar_lecciones
from agentes.curador import Biblioteca
from almacenamiento import Almacenamiento
from evolucion.builder import construir_candidatos
from evolucion.validador import comparar

def demo(modo="determinista", n=N_PERSONAS, semilla=SEMILLA):
    personas=generar_personas(n,semilla); guardar(personas)
    almacen=Almacenamiento()
    almacen.registrar_lote(f"lote-{semilla}-{n}",semilla,n)
    # Experimento longitudinal independiente: memoria vs línea base.
    con=copy.deepcopy(personas); sin=copy.deepcopy(personas)
    biblioteca=Biblioteca(); con_memoria=[]; sin_memoria=[]; historial=[]
    for ronda in range(RONDAS):
        tipo=TIPOS_PROYECTO[ronda % len(TIPOS_PROYECTO)]
        equipos=armar_equipos(con,tipo,biblioteca.relevantes(tipo),semilla=semilla+ronda)
        res=evaluar(equipos,tipo,ronda+1); historial.extend(res)
        score=sum(x["score"] for x in res)/len(res)
        actualizar_perfiles(con,res)
        propuestas=sacar_lecciones(res,con,tipo)
        for p in propuestas: biblioteca.agregar(p)
        con_memoria.append({"ronda":ronda+1,"tipo":tipo,"score_promedio":round(score,3),
                            "error_perfiles":_error(con),"lecciones":len(biblioteca.lecciones)})
        equipos0=armar_equipos(sin,tipo,[],semilla=semilla+ronda)
        res0=evaluar(equipos0,tipo,ronda+1)
        sin_memoria.append({"ronda":ronda+1,"tipo":tipo,
                            "score_promedio":round(sum(x["score"] for x in res0)/len(res0),3),
                            "error_perfiles":_error(sin),"lecciones":0})
    Path("resultados").mkdir(exist_ok=True)
    metricas={"con_memoria":con_memoria,"sin_memoria":sin_memoria,
              "personas":con,"reglas_ocultas":["El simulador premia combinaciones distintas por tipo de proyecto.",
              "Los perfiles reales solo son accesibles al simulador y al cálculo de error."]}
    Path("resultados/metricas.json").write_text(json.dumps(metricas,indent=2,ensure_ascii=False),encoding="utf-8")
    estrategia={"id":"v1","version_padre":None,"pesos":{"cumplimiento_lecciones":0.7,"balance":0.3},
                "presupuesto_busqueda":300,"lecciones":[],"schema_version":"1.0"}
    contexto={"tipo_proyecto":"todos","muestras":historial[:12],"perfiles_observables":[
        {k:v for k,v in p.items() if k!="real"} for p in con]}
    agente_resultado=None
    if modo=="api":
        from llm import analizar_con_subagentes_sync
        agente_resultado=analizar_con_subagentes_sync(contexto)
        Path("resultados/agentes.json").write_text(json.dumps(agente_resultado,indent=2,ensure_ascii=False),encoding="utf-8")
    # Validación de mecanismo: una estrategia inválida debe ser rechazada por contrato.
    try:
        from contratos import validar_estrategia
        invalida={**estrategia,"pesos":{"cumplimiento_lecciones":2,"balance":0}}
        validar_estrategia(invalida); rechazo=False
    except ValueError: rechazo=True
    evolucion={"schema_version":"1.0","modo":modo,"estrategia_vigente":estrategia,
               "candidatos":[],"rechazo_mecanismo_invalido":rechazo,
               "nota":"La demo no afirma mejora autónoma si no existe candidato con evidencia suficiente."}
    if modo=="api" and agente_resultado:
        evolucion["salida_subagentes"]=agente_resultado
    Path("resultados/evolucion.json").write_text(json.dumps(evolucion,indent=2,ensure_ascii=False),encoding="utf-8")
    almacen.registrar_experimento("demo-inicial",modo,{"rondas":RONDAS,"semilla":semilla})
    print("Demo lista: resultados/metricas.json y resultados/evolucion.json")
    print(f"Modo: {modo}. Error final de perfiles: {_error(con):.3f}")
    return metricas

def _error(personas):
    return round(sum(abs(p["estimado"][r]-p["real"][r]) for p in personas for r in RASGOS)/(len(personas)*len(RASGOS)),3)

def evaluar_versiones():
    print("La evaluación versionada se activa al generar propuestas con evidencia; consulta docs/evaluacion.md.")
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="TEAMFORGE")
    sub=parser.add_subparsers(dest="cmd",required=True)
    d=sub.add_parser("demo"); d.add_argument("--mode",choices=["determinista","api"],default="determinista")
    d.add_argument("--personas",type=int,default=N_PERSONAS); d.add_argument("--seed",type=int,default=SEMILLA)
    sub.add_parser("evaluar")
    a=parser.parse_args()
    if a.cmd=="demo": demo(a.mode,a.personas,a.seed)
    else: evaluar_versiones()
