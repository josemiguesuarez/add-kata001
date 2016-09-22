from unittest import TestCase
from Numeros import Numeros

class NumerosTest(TestCase):
    numeros = Numeros()

    def test_definirCadena (self):
        self.numeros.definirCadena("1,2,3,4,5")
        self.assertEqual(self.numeros.cadena, "1,2,3,4,5", "No definio la cadena")

    def test_arregloConNumeroElementos (self):
        self.numeros.definirCadena("")
        self.assertEqual(self.numeros.darArreglo()[0], 0, "No devolvio correctamente el numero de elementos")
