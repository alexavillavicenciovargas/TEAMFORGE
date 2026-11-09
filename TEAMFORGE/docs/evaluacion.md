# Evaluación y límites
**Propietario:** Persona 2

El simulador es un entorno sintético y su fórmula está congelada en `simulador.py`. Los efectos por proyecto son supuestos de diseño, no afirmaciones sobre personas reales.

## Reproducibilidad
- Semilla base: 42; cada operación usa `random.Random(seed)` local.
- Población inicial: 24 perfiles sintéticos.
- Rondas longitudinales: 10; alternan creativo, técnico y entrega rápida.
- Métricas longitudinales: score medio y error absoluto medio entre estimado y real.
- `con_memoria` y `sin_memoria` mantienen copias separadas.

## Protocolo objetivo para siguiente iteración
Separar descubrimiento, validación y prueba final reservada en manifiestos distintos. La prueba final se ejecuta una vez, después de seleccionar estrategia. Criterio demo: +2 puntos de media global y ninguna categoría cae más de 2. Informar n y dispersión. La primera versión implementa el simulador fijo y los contratos, pero aún no ejecuta el protocolo completo de holdout ni declara aprendizaje autónomo validado.

## Interpretación
Una asociación observada no demuestra causalidad. `error_perfiles` es una métrica de calibración sintética, no de calidad humana. No exigir mejora monótona.
