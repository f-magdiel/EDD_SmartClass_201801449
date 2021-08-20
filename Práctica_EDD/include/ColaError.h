#ifndef COLAERROR_H
#define COLAERROR_H
#include "NodoCola.h"
#include <string>


class ColaError
{
    public:
        ColaError();
        virtual ~ColaError();
        NodoCola* frente;
        NodoCola* fin;
        int tamanio=0;
        void encolar(string,string,string,string,string,string,string,string);
        void desencolar();
        void mostrarCola();
        void mostrarError();
};
extern ColaError colaDeError;
#endif // COLAERROR_H
