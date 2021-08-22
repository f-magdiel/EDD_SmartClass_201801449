#include "ColaError.h"
#include <string>
#include <iostream>
using namespace std;

ColaError::ColaError()
{
    this->frente = NULL;
    this->fin = NULL;
    this->tamanio = 0;
    this->contadorID =0;
}

void ColaError::encolar(int _id,string _tipo,string _descripcion,string _dpi){
    this->tamanio++;

    NodoCola* nuevoNodo = new NodoCola(_id,_tipo,_descripcion,_dpi);
    if(this->frente==NULL && this->fin==NULL){
        this->frente = nuevoNodo;
        this->fin = nuevoNodo;
    }else{
        this->fin->siguiente = nuevoNodo;
    }
    this->fin = nuevoNodo;
}

void ColaError::desencolar(){
    this->tamanio--;
    NodoCola* aux = this->frente;

    if(this->frente!=NULL){
        this->frente = aux->siguiente;
        //delete(aux);

    }else{
    cout << "   *Cola Vacia" << endl;
    }

}

void ColaError::mostrarError(){
    //Para reportar error

    if(this->tamanio!=0){
        cout << "   -Errores en la entrada: ";
        cout << this->tamanio << endl;
    }else{
        cout << "   -Errores en la entrada: ";
        cout << this->tamanio << endl;
    }
}

void ColaError::mostrarCola(){
    NodoCola* actual = this->frente;
    string res="";
    while(actual!=NULL){
        cout << "Id: ";
        cout << actual->id <<endl;
        cout << "Tipo: ";
        cout << actual->tipo << endl;
        cout << "Descripcion: ";
        cout << actual->descripcion << endl;
        cout << "DPI: ";
        cout << actual->dpi << endl;
        cout << "\n";
        actual = actual->siguiente;
    }

}

void ColaError::cima(string _dpi){
    if(_dpi == this->frente->dpi){
        cout << this->frente->dpi << endl;
        desencolar();
    }
}
ColaError::~ColaError()
{
    //dtor
}
