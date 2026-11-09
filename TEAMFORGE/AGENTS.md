# Instrucciones para agentes de código
- Mantener compatibilidad con contratos descritos en `docs/contratos.md`.
- No permitir `real` ni reglas ocultas en prompts de LLM, constructor o builder.
- Nunca modificar `simulador.py` para favorecer candidatos.
- No aceptar estrategias por su propia evaluación; usar benchmark fijo.
- Ejecutar `python -m unittest discover -s tests` antes de integrar.
- Documentar límites y no inventar resultados.
