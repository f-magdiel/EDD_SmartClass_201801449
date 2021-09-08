class Nodo:
    def __init__(self,_mes):
        self.mes = _mes
        self.siguiente = None
        self.anterior = None
        #apuntador matriz


class listaMes:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self,_mes):
        nuevoNodo = Nodo(_mes)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_mes):
        actual = self.cabeza
        while(actual!=None):
            if(_mes == actual.mes):
                return actual.mes
            
            actual = actual.siguiente

        return None


    def buscarAgregar(self,_mes):
        actual = self.cabeza
        banderaRepetido = False
        while(actual!=None):
            if(_mes==actual.mes):
                banderaRepetido = True
                break

            actual = actual.siguiente

        if(banderaRepetido == True):
            print("Mes ya existe")
        else:
            self.agregar(_mes) #en este metodo se agrega si no hay repeat en la lista

    def actualizar(self,_mes,_sustituto):
        actual = self.cabeza
        while(actual!=None):
            if(_mes == actual.mes):
                actual.mes = _sustituto
                break
            actual = actual.siguiente

    def eliminar(self,_mes):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.mes == _mes)
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


lista = listaMes()
lista.buscarAgregar("Mayo")
lista.buscarAgregar("Junio")
lista.buscarAgregar("Julio")
lista.buscarAgregar("Agosto")
lista.buscarAgregar("Septiembre")
lista.eliminar("Mayo")
print("Fin")