#include <iostream>
#include "Menu.h"
#include "ListaDobleCircular.h"
#include "ColaError.h"
#include "ArchivoTarea.h"
#include "Matriz.h"
#include "ListaDoble.h"
using namespace std;
ListaDoble listadoble;
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
    //para recorrer y linealizar matriz
    for(int z=0;z<5;z++){
        for (int i = 0;i<9;i++){
            for(int j = 0;j<30;j++){
                _k = (j*TJ+i)*TZ+z;
                matrizTareas[z][i][j]->setK(_k);
            }
        }
    }
    listadoble = ListaDoble();
    //se crea la lista al principio y se agrega la linealizacion #
    int linea;
    for(int i=0;i<30;i++){
        for (int j=0;j<9;j++){
            for(int k=0;k<5;k++){
                linea = matrizTareas[k][j][i]->k;
                listadoble.agregar(-1,"-1","-1","-1","-1","-1","-1","-1",linea);
            }
        }
    }


    listadc = ListaDobleCircular();
    colaDeError = ColaError();
    menuPrincipal();
    return 0;
}
