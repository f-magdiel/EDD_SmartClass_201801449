#include "NodoListaDoble.h"
#include <string>
#include <iostream>

using namespace std;
NodoListaDoble::NodoListaDoble(int _id,string _carnet,string _nombre,string _descripcion,string _materia,string _fecha,string _hora,string _estado,int _linea)
{
    this->id = _id;
    this->carnet = _carnet;
    this->nombre = _nombre;
    this->descripcion = _descripcion;
    this->materia = _materia;
    this->fecha = _fecha;
    this->hora = _hora;
    this->estado = _estado;
    this->linea = _linea;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodoListaDoble::~NodoListaDoble()
{
    //dtor
}
