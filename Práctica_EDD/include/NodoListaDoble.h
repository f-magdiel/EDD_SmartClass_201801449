#ifndef NODOLISTADOBLE_H
#define NODOLISTADOBLE_H
#include <string>
#include <iostream>
using namespace std;

class NodoListaDoble
{
    public:
        NodoListaDoble(int,string,string,string,string,string,string,string);
        virtual ~NodoListaDoble();
        int id;
        string carnet;
        string nombre;
        string descripcion;
        string materia;
        string fecha;
        string hora;
        string estado;
        NodoListaDoble* siguiente;
        NodoListaDoble* anterior;

};

#endif // NODOLISTADOBLE_H
