#ifndef NODOCOLA_H
#define NODOCOLA_H
#include <iostream>
#include <string>

using namespace std;

class NodoCola
{
    public:
        NodoCola(string,string,string,string,string,string,string,string);
        virtual ~NodoCola();

    string carnet;
    string dpi;
    string nombre;
    string carrera;
    string correo;
    string password;
    string creditos;
    string edad;

    NodoCola* siguiente;
};

#endif // NODOCOLA_H
