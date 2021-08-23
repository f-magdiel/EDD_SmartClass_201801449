#ifndef LISTADOBLECIRCULAR_H
#define LISTADOBLECIRCULAR_H
#include "NodoDobleCircular.h"
#include <string>

class ListaDobleCircular
{
    public:
        ListaDobleCircular();
        virtual ~ListaDobleCircular();
        NodoDobleCircular* cabeza;
        NodoDobleCircular* cola;

        void agregarInicio(string,string,string,string,string,string,string,string);
        void agregarFinal(string,string,string,string,string,string,string,string);
        void eliminar(string);
        void buscarModificar(string);
        void mostrar();
        bool buscar(string);
};

extern ListaDobleCircular listadc;

#endif // LISTADOBLECIRCULAR_H
