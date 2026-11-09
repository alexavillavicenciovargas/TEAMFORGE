# TEAMFORGE
Primera versión del hackathon KAVAK × OpenAI × Primero AI. Construye equipos con perfiles sintéticos, simula resultados, registra feedback y prepara estrategias declarativas. No reentrena modelos ni modifica su propio código.

## Inicio
Python 3.11+
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py demo
streamlit run app.py
```
macOS/Linux: `python3.11 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.

Modo multiagente real: define `OPENAI_API_KEY` como variable de entorno y ejecuta `python main.py demo --mode api`. Usa OpenAI Agents SDK: Analista de perfiles → Estratega de equipos → Revisor independiente. El modo determinista no requiere llave.

## Validación
`python -m unittest discover -s tests`

## Arquitectura
- Núcleo reproducible: perfiles, simulador, constructor, evaluador, reflexión y biblioteca.
- OpenAI: especialistas Agents SDK opcionales; nunca reciben perfiles reales ni reglas ocultas.
- UI: Streamlit lee JSON persistido.
- Persistencia: SQLite para lotes, experimentos, evidencias y versiones.

Consulta `docs/contratos.md`, `docs/evaluacion.md` y `docs/demo.md`. La comparación final con holdout reservado y aceptación persistente de candidatos queda como siguiente hito; no se afirma mejora autónoma demostrada.