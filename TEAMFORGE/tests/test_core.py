import unittest, tempfile
from pathlib import Path
from personas import generar_personas
from agentes.constructor import armar_equipos
from agentes.reflexionador import actualizar_perfiles
from contratos import validar_estrategia

class TeamforgeTests(unittest.TestCase):
    def test_reproducibilidad(self):
        self.assertEqual(generar_personas(24,7),generar_personas(24,7))
    def test_perfiles_rango_y_esquema(self):
        for p in generar_personas():
            self.assertEqual(set(p),{"id","nombre","declarado","real","estimado"})
            for k in ("declarado","real","estimado"):
                self.assertTrue(all(1 <= v <= 5 for v in p[k].values()))
    def test_reparto_sin_duplicados(self):
        ps=generar_personas()
        eq=armar_equipos(ps,"creativo",[],semilla=9)
        ids=[p["id"] for e in eq for p in e]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),{p["id"] for p in ps})
    def test_divisibilidad(self):
        with self.assertRaises(ValueError): armar_equipos(generar_personas(10),"creativo",[])
    def test_actualizacion_en_sitio(self):
        ps=generar_personas(4); before=ps[0]["estimado"]["creatividad"]
        actualizar_perfiles(ps,[{"feedback":{ps[0]["id"]:{"creatividad":5}}}])
        self.assertNotEqual(before,ps[0]["estimado"]["creatividad"])
    def test_pesos(self):
        self.assertTrue(validar_estrategia({"schema_version":"1.0","pesos":{"cumplimiento_lecciones":.7,"balance":.3},"presupuesto_busqueda":100}))
        with self.assertRaises(ValueError):
            validar_estrategia({"schema_version":"1.0","pesos":{"cumplimiento_lecciones":2,"balance":0},"presupuesto_busqueda":100})
if __name__=="__main__": unittest.main()
