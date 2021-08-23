#include "ListaDoble.h"
#include <string>
#include <iostream>

using namespace std;
ListaDoble::ListaDoble()
{
    this->cabeza = NULL;
    this->cola = NULL;
}

void ListaDoble::agregar(int _id,string _carnet,string _nombre,string _descripcion,string _materia,string _fecha,string _hora,string _estado){
    NodoListaDoble* nuevoNodo = new NodoListaDoble(_id,_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado);
    if(!this->cabeza){
        this->cabeza = nuevoNodo;
    }else{
        NodoListaDoble* actual = this->cabeza;
        while(actual->siguiente!=NULL){
            actual = actual->siguiente;
        }
        actual->siguiente = nuevoNodo;
        nuevoNodo->anterior = actual;
        this->cola = nuevoNodo;
    }

}

void ListaDoble::buscar(int _id){
    NodoListaDoble* actual = this->cabeza;
    while(actual!=NULL){
        if(_id==actual->id){
            cout << "Si esta" << endl;
        }
        actual = actual->siguiente;
    }
}

void ListaDoble::actualizar(int _id){
    NodoListaDoble* actual = this->cabeza;
    while(actual!=NULL){
        if(_id==actual->id){
            string opcion;
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
            printf("%c     MODIFICAR    %c\n",186,186);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
            printf("%c  [1] Carnet        %c\n",186,186);
            printf("%c  [2] Nombre Tarea  %c\n",186,186);
            printf("%c  [3] Descripcion   %c\n",186,186);
            printf("%c  [4] Materia       %c\n",186,186);
            printf("%c  [5] Fecha         %c\n",186,186);
            printf("%c  [6] Hora          %c\n",186,186);
            printf("%c  [7] Estado        %c\n",186,186);
            printf("%c  [8] Regresar      %c\n",186,186);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
            cout << "   -Ingrese una opcion >> ";
            getline(cin,opcion);
            break;
        }
        actual = actual->siguiente;
    }
}

ListaDoble::~ListaDoble()
{
    //dtor
}
