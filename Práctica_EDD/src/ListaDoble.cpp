#include "ListaDoble.h"
#include <string>
#include <iostream>

using namespace std;
ListaDoble::ListaDoble()
{
    this->cabeza = NULL;
    this->cola = NULL;
}

void ListaDoble::agregar(int _id,string _carnet,string _nombre,string _descripcion,string _materia,string _fecha,string _hora,string _estado,int _linea){
    NodoListaDoble* nuevoNodo = new NodoListaDoble(_id,_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);
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

void ListaDoble::buscarAgregar(int _id,string _carnet,string _nombre,string _descripcion,string _materia,string _fecha,string _hora,string _estado,int _linea){
    NodoListaDoble* actual = this->cabeza;
    while(actual!=NULL){
        if(_linea==actual->linea){
            actual->id = _id;
            actual->carnet = _carnet;
            actual->nombre = _nombre;
            actual->descripcion = _descripcion;
            actual->materia = _materia;
            actual->fecha = _fecha;
            actual->hora = _hora;
            actual->estado = _estado;
            break;
        }
        actual = actual->siguiente;
    }
}

void ListaDoble::actualizar(string _carnet,string _nombre,string _descripcion,string _materia,string _fecha,string _hora,string _estado,int _linea){
    NodoListaDoble* actual = this->cabeza;
    while(actual!=NULL){
        if(_linea==actual->linea){
            actual->carnet = _carnet;
            actual->nombre = _nombre;
            actual->descripcion = _descripcion;
            actual->materia = _materia;
            actual->fecha = _fecha;
            actual->hora = _hora;
            actual->estado = _estado;
            break;
        }
        actual = actual->siguiente;
    }
}

void ListaDoble::eliminar(int _id){
    NodoListaDoble* actual = this->cabeza;
}

void ListaDoble::imprimir(){
    cout << "IMPRESION"<<endl;
    NodoListaDoble* actual = this->cabeza;
    while(actual!=NULL){
        cout << actual->carnet;
        cout << " ";
        actual = actual->siguiente;
    }
}
ListaDoble::~ListaDoble()
{
    //dtor
}
