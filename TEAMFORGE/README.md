# TEAMFORGE
**Hackathon KAVAK × OpenAI × Primero AI — primera versión**

TEAMFORGE forma equipos sintéticos, observa resultados de un simulador, registra lecciones y prepara la base para comparar estrategias. No reentrena el modelo ni modifica su propio código. La evolución se limita a configuraciones declarativas.

## Requisitos
- Python 3.11+
- Streamlit para el panel
- OpenAI Agents SDK solo para el modo API

## Arranque — Windows PowerShell
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py demo
streamlit run app.py
```
Para usar subagentes:
```powershell
$env:OPENAI_API_KEY = "tu_api_key"
$env:OPENAI_MODEL = "gpt-5.5"
python main.py demo --mode api
```

## macOS / Linux
```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py demo
streamlit run app.py
```
Modo API: `export OPENAI_API_KEY="tu_api_key"` y `python main.py demo --mode api`.

## Comandos
- `python main.py demo`: ciclo longitudinal reproducible sin API.
- `python main.py demo --mode api`: invoca tres agentes especialistas mediante OpenAI Agents SDK.
- `python main.py evaluar`: muestra la ruta documentada para evaluación versionada.
- `python -m unittest discover -s tests`: pruebas.
- `streamlit run app.py`: interfaz.

## Arquitectura de subagentes
1. **Analista de perfiles:** resume solo atributos observables y evidencia agregada.
2. **Estratega de equipos:** sugiere cambios declarativos, sin tocar evaluador ni simulador.
3. **Revisor independiente:** audita evidencia, restricciones y riesgos.

Cada especialista es un `Agent` del SDK ejecutado por `Runner`; si falla la API, la demo determinista sigue disponible. Las salidas LLM se registran como propuestas, no se aceptan automáticamente.

## Propiedad de archivos (equipo de cuatro)
- Persona 1: `config.py`, `agentes/constructor.py`, `agentes/evaluador.py`, `contratos.py`, `evolucion/motor.py`, `evolucion/validador.py`, `main.py`.
- Persona 2: `personas.py`, `simulador.py`, `almacenamiento.py`, `benchmark.py`, `docs/evaluacion.md`.
- Persona 3: `llm.py`, `agentes/reflexionador.py`, `agentes/curador.py`, `evolucion/builder.py`, `skills/`.
- Persona 4: `app.py`, `README.md`, `docs/demo.md`.

## Estado honesto de esta versión
Funciona la generación sintética, simulación, memoria longitudinal, JSON compatible, SQLite básico, panel y ejecución opcional de subagentes. La comparación completa con tres particiones independientes, holdout reservado, generación de casos de regresión integrados y aceptación persistente de candidatos queda como siguiente hito. No se afirma que el sistema ya haya demostrado una mejora autónoma.

## Seguridad
No guardes la API key en el repositorio. Usa variables de entorno; `.env.example` es solo una plantilla. No subas `.env`.
