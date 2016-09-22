from unittest import TestCase
from Numeros import Numeros

class NumerosTest(TestCase):
    numeros = Numeros()

    def test_definirCadena (self):
        self.numeros.definirCadena("1,2,3,4,5")
        self.assertEqual(self.numeros.cadena, "1,2,3,4,5", "No definio la cadena")

    def test_darNumeroDeElementos (self):
        self.numeros.definirCadena("")
        self.assertEqual(self.numeros.darArreglo()[0], 0, "No devolvio correctamente el numero de elementos")

        self.numeros.definirCadena("1")
        self.assertEqual(self.numeros.darArreglo()[0], 1, "No devolvio correctamente el numero de elementos")

        self.numeros.definirCadena("1,2")
        self.assertEqual(self.numeros.darArreglo()[0], 2, "No devolvio correctamente el numero de elementos")

        self.numeros.definirCadena("1,2")
        self.assertEqual(self.numeros.darArreglo()[0], 2, "No devolvio correctamente el numero de elementos")

        self.numeros.definirCadena("1,2,3,4,5,6,7")
        self.assertEqual(self.numeros.darArreglo()[0], 7, "No devolvio correctamente el numero de elementos")



