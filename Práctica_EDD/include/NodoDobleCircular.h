#ifndef NODODOBLECIRCULAR_H
#define NODODOBLECIRCULAR_H
#include <iostream>
#include <string>

using namespace std;
class NodoDobleCircular
{
    public:
        NodoDobleCircular(string,string,string,string,string,string,string,string);
        virtual ~NodoDobleCircular();

    string carnet;
    string dpi;
    string nombre;
    string carrera;
    string correo;
    string password;
    string creditos;
    string edad;

    NodoDobleCircular* siguiente;
    NodoDobleCircular* anterior;
};

#endif // NODODOBLECIRCULAR_H
