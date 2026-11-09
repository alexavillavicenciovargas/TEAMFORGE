# Guion de demo (4 horas)
1. `python main.py demo` genera 24 perfiles, 10 rondas y `resultados/metricas.json`.
2. `streamlit run app.py` abre score/error de ambas condiciones.
3. `python main.py demo --mode api` ejecuta los subagentes OpenAI si existe `OPENAI_API_KEY`; crea `resultados/agentes.json`.
4. Revisar `resultados/evolucion.json`: configuración, modo y prueba explícita de rechazo por estrategia inválida.
5. Explicar qué permanece fijo: simulador, métrica externa y código. Lo que cambia son parámetros y reglas declarativas.

No afirmar que el modelo se reentrena, que modifica código o que la mejora es universal.
