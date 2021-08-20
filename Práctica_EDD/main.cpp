#include <iostream>
#include "Menu.h"
#include "ListaDobleCircular.h"
#include "ColaError.h"

using namespace std;
ListaDobleCircular listadc;
ColaError colaDeError;
int main()
{
    listadc = ListaDobleCircular();
    colaDeError = ColaError();
    menuPrincipal();
    return 0;
}
