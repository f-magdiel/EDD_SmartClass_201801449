#ifndef NODOLISTADOBLE_H
#define NODOLISTADOBLE_H
#include <string>
#include <iostream>
using namespace std;

class NodoListaDoble
{
    public:
        NodoListaDoble(int,string,string,string,string,string,string,string,int);
        virtual ~NodoListaDoble();
        int id;
        string carnet;
        string nombre;
        string descripcion;
        string materia;
        string fecha;
        string hora;
        string estado;
        int linea;
        NodoListaDoble* siguiente;
        NodoListaDoble* anterior;

};

#endif // NODOLISTADOBLE_H
