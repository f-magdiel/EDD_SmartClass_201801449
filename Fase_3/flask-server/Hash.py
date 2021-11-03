class Nodo:
    def __init__(self, indice):
        self.indice = indice
        self.lista = []

class Llave:
    def __init__(self,indice, titulo, contenido):
        self.indice = indice
        self.titulo = titulo
        self.contenido = contenido
    def print(self):
        return "titulo:"+self.titulo + ", contenido:"+ self.contenido

class Hash:
    def __init__(self, contenido=7):
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamano = contenido

        for i in range(contenido):
            self.vector.append(None)

    def insertar(self, id, titulo, contenido):
        posicion = self.funcion_hash(id)
        
        if self.vector[posicion] != None:
            nuevo_contenido = Llave(id,titulo,contenido)
            self.vector[posicion].lista.append(nuevo_contenido)
        else:
            nuevo = Nodo(posicion)
            nuevo.lista.append(Llave(id,titulo, contenido))
            self.vector[posicion] = nuevo
            self.elementos+=1
            self.factorCarga = self.elementos/self.tamano

        if self.factorCarga > 0.5:
            self.rehashing()

    def rehashing(self):
        siguiente = self.tamano
        factor = 0
        while(factor < 0.3):
            factor = self.elementos/siguiente
            siguiente +=1

        temporal = []
        self.elementos = 0
        
        for i in range(siguiente):
            temporal.append(None)

        aux_vector = self.vector

        self.vector = temporal
        self.tamano = siguiente

        print("Nuevo tamano", siguiente, "Tamano:", len(temporal))
        for i in aux_vector:
            if i:
                for j in i.lista:
                    self.insertar(j.indice, j.titulo, j.contenido)


    def funcion_hash(self, id):
        posicion = id % (self.tamano-1)
        if posicion > self.tamano:
            return posicion - self.tamano
        return posicion



    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("indice:",contador, "contenido:", [j.print() for j in i.lista] )
            else:
                print("indice:", contador, "contenido", i)

            contador+=1

def toASCII(cadena):
    result = 0
    for char in cadena:
        result += ord(char)
    return result


tabla = Hash()
tabla.insertar(201801449,"primero","ocupado")
tabla.insertar(202102237,"casa","colision")
tabla.insertar(201801449,"saca","colision")
tabla.insertar(201501456,"saca1","colision")
tabla.insertar(202102234,"saca2","no hay colision")
tabla.insertar(201801440,"saca3","1")
tabla.print()