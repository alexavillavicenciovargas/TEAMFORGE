"""Persona 1 — Contratos versionados."""
SCHEMA_VERSION="1.0"
def validar_estrategia(e):
 if e.get("schema_version")!=SCHEMA_VERSION: raise ValueError("Esquema incompatible")
 p=e.get("pesos",{})
 if set(p)!={"cumplimiento_lecciones","balance"} or any(not isinstance(v,(int,float)) or v<0 for v in p.values()) or abs(sum(p.values())-1)>1e-8: raise ValueError("Pesos inválidos")
 if not 1<=e.get("presupuesto_busqueda",0)<=300: raise ValueError("Presupuesto inválido")
 return True