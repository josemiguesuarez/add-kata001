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
            min2 = float('inf')
        else:
            min2 = min(arregloInts)


        return [len(arregloInts), min2, -float('inf')]