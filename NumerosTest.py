from unittest import TestCase
from Numeros import Numeros

class NumerosTest(TestCase):
    numeros = Numeros()
    
    def test_definirCadena (self):
        self.numeros.definirCadena("1,2,3,4,5")
