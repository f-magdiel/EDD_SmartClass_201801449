class Nodo:
    def __init__(self,_year):
        self.year = _year
        self.siguiente = None
        self.anterior = None
        #apuntador semestre
        #apuntador mes


class listaAño:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self,_year):
        nuevoNodo = Nodo(_year)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_year):
        actual = self.cabeza
        while(actual!=None):
            if(_year == actual.year):
                return actual.year
            
            actual = actual.siguiente

        return None


    def buscarAgregar(self,_year):
        actual = self.cabeza
        banderaRepetido = False
        while(actual!=None):
            if(_year==actual.year):
                banderaRepetido = True
                break

            actual = actual.siguiente

        if(banderaRepetido == True):
            print("Dato ya existe")
        else:
            self.agregar(_year) #en este metodo se agrega si no hay repeat en la lista

    def actualizar(self,_year,_sustituto):
        actual = self.cabeza
        while(actual!=None):
            if(_year == actual.year):
                actual.year = _sustituto
                break
            actual = actual.siguiente

    def eliminar(self,_year):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.year == _year)
            if(encontrado == False):
                actual = actual.siguiente

        if(actual!=None):
            if(actual == self.cabeza):
                self.cabeza = actual.siguiente
                if(actual.siguiente!=None):
                    actual.siguiente.anterior = None
            elif(actual.siguiente!=None):
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
            else:
                actual.anterior.siguiente = None
                self.cola = actual.anterior
                actual = None


lista = listaAño()
lista.buscarAgregar(12)
lista.buscarAgregar(13)
lista.buscarAgregar(14)
lista.buscarAgregar(15)
lista.buscarAgregar(16)
lista.eliminar(12)
print("Fin")