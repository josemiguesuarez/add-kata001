class Numeros:
    cadena = ""
    def definirCadena (self, cadena):
        self.cadena = cadena

    def darArreglo (self):
        arreglo = self.cadena.split(",")
        for item in arreglo:
            if item == '':
                arreglo.remove(item)

        return [len(arreglo), 0]