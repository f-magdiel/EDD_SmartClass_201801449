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
    int TZ = 5; //caras
    int TJ = 9;
    int _k=0;
    //para recorrer y linealizar
    for(int z=0;z<5;z++){
        for (int i = 0;i<9;i++){
            for(int j = 0;j<30;j++){
                _k = (j*TJ+i)*TZ+z;
                matrizTareas[z][i][j]->setK(_k);
            }
        }
    }

    //matrizTareas[0][0][0] ->insertar("nombre","dato");
    listadc = ListaDobleCircular();
    colaDeError = ColaError();
    menuPrincipal();
    return 0;
}
