"""Persona 4 — UI Streamlit basada en resultados persistidos."""
import json
from pathlib import Path
import streamlit as st
st.set_page_config(page_title="TEAMFORGE",layout="wide"); st.title("TEAMFORGE"); st.caption("Simulación sintética · estrategias iterativas · evidencia")
p=Path("resultados/metricas.json")
if not p.exists(): st.warning("Ejecuta python main.py demo"); st.stop()
d=json.loads(p.read_text(encoding="utf-8")); a,b=st.columns(2)
with a: st.subheader("Score por ronda"); st.line_chart({"Con memoria":[x["score_promedio"] for x in d["con_memoria"]],"Sin memoria":[x["score_promedio"] for x in d["sin_memoria"]]})
with b: st.subheader("Error de perfiles"); st.line_chart({"Con memoria":[x["error_perfiles"] for x in d["con_memoria"]],"Sin memoria":[x["error_perfiles"] for x in d["sin_memoria"]]})
st.subheader("Rondas"); st.dataframe(d["con_memoria"],use_container_width=True); st.caption(f"Perfiles sintéticos: {len(d['personas'])}")