import unittest
from personas import generar_personas
from simulador import simular
class SimulatorTests(unittest.TestCase):
    def test_simulacion_reproducible(self):
        e=generar_personas(4)
        self.assertEqual(simular(e,"tecnico",10),simular(e,"tecnico",10))
    def test_rango(self):
        r=simular(generar_personas(4),"creativo",1)
        self.assertTrue(0 <= r["score"] <= 100)
        self.assertTrue(all(1 <= v <= 5 for p in r["feedback"].values() for v in p.values()))
if __name__=="__main__": unittest.main()
