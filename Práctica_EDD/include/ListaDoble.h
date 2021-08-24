#ifndef LISTADOBLE_H
#define LISTADOBLE_H
#include "NodoListaDoble.h"
#include <iostream>
#include <string>

using namespace std;

class ListaDoble
{
    public:
        ListaDoble();
        virtual ~ListaDoble();

   void agregar(int,string,string,string,string,string,string,string,int);
   void buscarAgregar(int,string,string,string,string,string,string,string,int);
   void actualizar(string,string,string,string,string,string,string,int);
   void eliminar(int);
   void imprimir();
   void generadorImagen();
   NodoListaDoble* cabeza;
   NodoListaDoble* cola;

};

extern ListaDoble listadoble;

#endif // LISTADOBLE_H
