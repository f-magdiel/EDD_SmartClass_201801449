#include "ColaError.h"
#include <string>
#include <iostream>
using namespace std;

ColaError::ColaError()
{
    this->frente = NULL;
    this->fin = NULL;
    this->tamanio = 0;
}

void ColaError::encolar(string _carnet,string _dpi, string _nombre, string _carrera, string _pass,string _creditos, string _edad, string _correo){
    this->tamanio++;

    NodoCola* nuevoNodo = new NodoCola(_carnet,_dpi,_nombre,_carrera,_pass,_creditos,_edad,_correo);
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
ColaError::~ColaError()
{
    //dtor
}
