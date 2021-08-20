#include "NodoDobleCircular.h"
#include <string>
#include <iostream>

using namespace std;

NodoDobleCircular::NodoDobleCircular(string _carnet,string _dpi, string _nombre, string _carrera, string _pass,string _creditos, string _edad, string _correo)
{
   this->carnet = _carnet;
   this->dpi = _dpi;
   this->nombre = _nombre;
   this->carrera = _carrera;
   this->correo = _correo;
   this->password = _pass;
   this->creditos = _creditos;
   this->edad = _edad;
   this->siguiente = NULL;
   this->anterior = NULL;
}

NodoDobleCircular::~NodoDobleCircular()
{
    //dtor
}
