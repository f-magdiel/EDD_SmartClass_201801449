#include <iostream>
#include "Menu.h"
#include "ListaDobleCircular.h"
#include "ColaError.h"
#include "ArchivoTarea.h"
#include "Matriz.h"

using namespace std;
ListaDobleCircular listadc;
ColaError colaDeError;
ArchivoTarea archivoTarea;
Matriz* matrizTareas [5][9][30]; //  Cara Filas columnas
int main()
{
    for(int i=0;i<5;i++){
        for (int j = 0;j<9;j++){
            for(int k = 0;k<30;k++){
                matrizTareas[i][j][k] = new Matriz();
            }
        }
    }

    //matrizTareas[0][0][0] ->insertar("nombre","dato");
    listadc = ListaDobleCircular();
    colaDeError = ColaError();
    menuPrincipal();
    return 0;
}
