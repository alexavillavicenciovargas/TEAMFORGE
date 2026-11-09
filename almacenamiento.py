"""Persona 2 — Persistencia SQLite."""
import sqlite3
from pathlib import Path
class Almacenamiento:
 def __init__(self,ruta="resultados/teamforge.sqlite3"):
  Path(ruta).parent.mkdir(parents=True,exist_ok=True); self.db=sqlite3.connect(ruta)
  self.db.executescript("CREATE TABLE IF NOT EXISTS lotes(id TEXT PRIMARY KEY,semilla INTEGER,cantidad INTEGER,creado TEXT DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS experimentos(id TEXT PRIMARY KEY,modo TEXT,datos TEXT,creado TEXT DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS evidencias(id TEXT PRIMARY KEY,experimento_id TEXT,datos TEXT); CREATE TABLE IF NOT EXISTS versiones(id TEXT PRIMARY KEY,padre TEXT,estrategia TEXT,decision TEXT,creado TEXT DEFAULT CURRENT_TIMESTAMP);")
 def registrar_lote(self,i,s,n):
  with self.db: self.db.execute("INSERT OR REPLACE INTO lotes(id,semilla,cantidad) VALUES(?,?,?)",(i,s,n))
 def registrar_experimento(self,i,m,d):
  import json
  with self.db: self.db.execute("INSERT OR REPLACE INTO experimentos(id,modo,datos) VALUES(?,?,?)",(i,m,json.dumps(d)))