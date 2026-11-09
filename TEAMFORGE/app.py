"""Persona 4 — Panel Streamlit; solo lee resultados persistidos."""
import json
from pathlib import Path
import streamlit as st
st.set_page_config(page_title="TEAMFORGE",layout="wide")
st.title("TEAMFORGE")
st.caption("Equipos sintéticos · aprendizaje iterativo de estrategias · evidencia reproducible")
p=Path("resultados/metricas.json")
if not p.exists():
    st.warning("Aún no hay métricas. Ejecuta: python main.py demo")
    st.stop()
data=json.loads(p.read_text(encoding="utf-8"))
a,b=st.columns(2)
with a:
    st.subheader("Score por ronda")
    st.line_chart({"Con memoria":[x["score_promedio"] for x in data["con_memoria"]],
                   "Sin memoria":[x["score_promedio"] for x in data["sin_memoria"]]})
with b:
    st.subheader("Error de perfiles")
    st.line_chart({"Con memoria":[x["error_perfiles"] for x in data["con_memoria"]],
                   "Sin memoria":[x["error_perfiles"] for x in data["sin_memoria"]]})
st.subheader("Evolución de estrategia")
ep=Path("resultados/evolucion.json")
if ep.exists():
    ev=json.loads(ep.read_text(encoding="utf-8"))
    st.write("Modo:",ev.get("modo","determinista"))
    st.json(ev)
st.subheader("Lecciones y rondas")
st.dataframe(data["con_memoria"],use_container_width=True)
st.caption(f"Perfiles sintéticos: {len(data['personas'])}. La verdad sintética se muestra solo en el artefacto local de demo.")
