#include "NodoCola.h"
#include <string>
#include <iostream>

using namespace std;
NodoCola::NodoCola(int _id,string _tipo, string _descripcion, string _dpi )
{
   this->id = _id;
   this->descripcion = _descripcion;
   this->tipo = _tipo;
   this->dpi = _dpi;
   this->siguiente = NULL;
}

NodoCola::~NodoCola()
{
    //dtor
}
