#ifndef NODOCOLA_H
#define NODOCOLA_H
#include <iostream>
#include <string>

using namespace std;

class NodoCola
{
    public:
        NodoCola(int,string,string,string);
        virtual ~NodoCola();
    int id;
    string tipo;
    string descripcion;
    string dpi;


    NodoCola* siguiente;
};

#endif // NODOCOLA_H
