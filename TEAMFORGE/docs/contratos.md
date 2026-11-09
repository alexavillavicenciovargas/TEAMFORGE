# Contratos de TEAMFORGE
**Propietario:** Persona 1 · Esquemas: 1.0

- Persona base: `id`, `nombre`, `declarado`, `real`, `estimado`; cada perfil contiene los cinco rasgos 1–5.
- Constructor y agentes de reflexión reciben perfiles observables sin `real`.
- Lección: `id`, `tipo_proyecto`, `rasgo`, `umbral`, `operador`, `cantidad`, `texto`, `veces_vista`, `veces_aplicada`, `veces_ayudo`.
- Identidad de lección: `(tipo_proyecto, rasgo, operador, umbral, cantidad)`. Esta corrección evita fusionar reglas con cantidades distintas. `agregar` devuelve `(lección, es_nueva)`.
- Estrategia 1.0: `id`, `version_padre`, `pesos`, `presupuesto_busqueda`, `lecciones`, `schema_version`.
- Propuesta 1.0: `id`, `estrategia`, `motivacion`, `evidencia_ids`, `schema_version`.
- Caso 1.0: `id`, `entrada`, `condicion`, `evidencia`, `resultado_esperado`, `schema_version`.
- Decisión 1.0: `id`, `candidato_id`, `aceptada`, `motivo`, `metricas`, `schema_version`.
- El almacenamiento nuevo vive en SQLite. JSON conserva la salida longitudinal compatible.
- El simulador y cálculo explícito de error pueden consultar `real`; el constructor, builder y prompts de agentes no deben recibirlo.
