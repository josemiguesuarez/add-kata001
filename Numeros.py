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
            max2 = -float('inf')
            prom = 0.0
        else:
            min2 = min(arregloInts)
            max2 = max(arregloInts)
            prom = float(sum(arregloInts))/len(arregloInts)


        return [len(arregloInts), min2, max2, prom]