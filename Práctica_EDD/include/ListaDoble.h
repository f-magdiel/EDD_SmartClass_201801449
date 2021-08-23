#ifndef LISTADOBLE_H
#define LISTADOBLE_H
#include "NodoListaDoble.h"
#include <iostream>
using namespace std;

class ListaDoble
{
    public:
        ListaDoble();
        virtual ~ListaDoble();

   void agregar(int,string,string,string,string,string,string,string);
   void buscar(int);
   void actualizar(int);
   void eliminar(int);
   NodoListaDoble* cabeza;
   NodoListaDoble* cola;

};

#endif // LISTADOBLE_H
