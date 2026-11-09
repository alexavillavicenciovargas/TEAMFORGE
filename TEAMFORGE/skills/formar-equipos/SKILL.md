# Skill: formar equipos
**Propietario:** Persona 3 · **Versión:** 1.0

## Propósito
Aplicar lecciones observables para formar equipos de cuatro sin consultar perfiles reales.

## Entradas
Personas con `id`, `nombre`, `declarado`, `estimado`; tipo de proyecto; lecciones compatibles; semilla.

## Procedimiento
1. Validar que el tamaño de población sea divisible entre cuatro.
2. Generar hasta 300 particiones reproducibles con RNG local.
3. Minimizar incumplimientos de lecciones.
4. Desempatar minimizando el rango entre medias de rasgos estimados dentro de cada equipo.

## Salida
Lista de equipos sin duplicados. La skill describe la conducta implementada en `agentes/constructor.py`.

## Límites
Las correlaciones son hipótesis sintéticas. No usar `real` ni reglas ocultas para construir equipos.
