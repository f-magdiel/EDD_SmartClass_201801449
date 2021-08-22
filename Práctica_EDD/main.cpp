#include <iostream>
#include "Menu.h"
#include "ListaDobleCircular.h"
#include "ColaError.h"
#include "ArchivoTarea.h"

using namespace std;
ListaDobleCircular listadc;
ColaError colaDeError;
ArchivoTarea archivoTarea;
int main()
{
    listadc = ListaDobleCircular();
    colaDeError = ColaError();
    menuPrincipal();
    return 0;
}
