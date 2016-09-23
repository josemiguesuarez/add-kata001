from unittest import TestCase
from Numeros import Numeros

class NumerosTest(TestCase):
    numeros = Numeros()

    def escenario1 (self):
        self.numeros.definirCadena("")

    def escenario2(self):
        self.numeros.definirCadena("1")

    def escenario3(self):
        self.numeros.definirCadena("1,2")

    def escenario4(self):
        self.numeros.definirCadena("6,2,3,2,5,6,7")

    def test_definirCadena (self):
        self.numeros.definirCadena("1,2,3,4,5")
        self.assertEqual(self.numeros.cadena, "1,2,3,4,5", "No definio la cadena")

    def test_darNumeroDeElementos (self):
        self.escenario1()
        self.assertEqual(self.numeros.darArreglo()[0], 0, "No devolvio correctamente el numero de elementos")

        self.escenario2()
        self.assertEqual(self.numeros.darArreglo()[0], 1, "No devolvio correctamente el numero de elementos")

        self.escenario3()
        self.assertEqual(self.numeros.darArreglo()[0], 2, "No devolvio correctamente el numero de elementos")

        self.escenario4()
        self.assertEqual(self.numeros.darArreglo()[0], 7, "No devolvio correctamente el numero de elementos")

    def test_darMinimo(self):
        self.escenario1()
        self.assertEqual(self.numeros.darArreglo()[1], float('inf'), "No devolvio correctamente el minimo de los elementos")

        self.escenario2()
        self.assertEqual(self.numeros.darArreglo()[1], 1, "No devolvio correctamente el minimo de los elementos")

        self.escenario3()
        self.assertEqual(self.numeros.darArreglo()[1], 1, "No devolvio correctamente el minimo de los elementos")

        self.escenario4()
        self.assertEqual(self.numeros.darArreglo()[1], 2, "No devolvio correctamente el minimo de los elementos")

    def test_darMaximo(self):
        self.escenario1()
        self.assertEqual(self.numeros.darArreglo()[2], -float('inf'), "No devolvio correctamente el maximo de los elementos")

        self.escenario2()
        self.assertEqual(self.numeros.darArreglo()[2], 1, "No devolvio correctamente el maximo de los elementos")

        self.escenario3()
        self.assertEqual(self.numeros.darArreglo()[2], 2, "No devolvio correctamente el maximo de los elementos")

        self.escenario4()
        self.assertEqual(self.numeros.darArreglo()[2], 7, "No devolvio correctamente el maximo de los elementos")

    def test_darPromedio(self):
        self.escenario1()
        self.assertEqual(self.numeros.darArreglo()[3], float('nan'), "No devolvio correctamente el promedio de los elementos")


