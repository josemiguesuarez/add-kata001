class Numeros:
    cadena = ""
    def definirCadena (self, cadena):
        self.cadena = cadena

    def darArreglo (self):
        arreglo = self.cadena.split(",")
        arregloInts = []
        for item in arreglo:
            if item == '':
                arreglo.remove(item)
            else:
                arregloInts.append(int(item))

        if(len(arregloInts) == 0):
            min = 0
        else:
            min = arregloInts[0]


        return [len(arregloInts), min]