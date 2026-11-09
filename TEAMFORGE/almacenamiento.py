"""Persona 2 — SQLite para experimentos, evidencias, lotes y decisiones."""
import sqlite3, json
from pathlib import Path
class Almacenamiento:
    def __init__(self, ruta="resultados/teamforge.sqlite3"):
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        self.db=sqlite3.connect(ruta)
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS lotes(id TEXT PRIMARY KEY, semilla INTEGER, cantidad INTEGER, creado TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS experimentos(id TEXT PRIMARY KEY, modo TEXT, datos TEXT, creado TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS evidencias(id TEXT PRIMARY KEY, experimento_id TEXT, datos TEXT, FOREIGN KEY(experimento_id) REFERENCES experimentos(id));
        CREATE TABLE IF NOT EXISTS versiones(id TEXT PRIMARY KEY, padre TEXT, estrategia TEXT, decision TEXT, creado TEXT DEFAULT CURRENT_TIMESTAMP);
        """)
        self.db.commit()
    def registrar_lote(self, id, semilla, cantidad):
        with self.db: self.db.execute("INSERT OR REPLACE INTO lotes(id,semilla,cantidad) VALUES(?,?,?)",(id,semilla,cantidad))
    def registrar_experimento(self, id, modo, datos):
        with self.db: self.db.execute("INSERT OR REPLACE INTO experimentos(id,modo,datos) VALUES(?,?,?)",(id,modo,json.dumps(datos)))
    def registrar_evidencia(self, id, experimento_id, datos):
        with self.db: self.db.execute("INSERT OR REPLACE INTO evidencias VALUES(?,?,?)",(id,experimento_id,json.dumps(datos)))
    def registrar_version(self, id, padre, estrategia, decision):
        with self.db: self.db.execute("INSERT OR REPLACE INTO versiones(id,padre,estrategia,decision) VALUES(?,?,?,?)",(id,padre,json.dumps(estrategia),json.dumps(decision)))
