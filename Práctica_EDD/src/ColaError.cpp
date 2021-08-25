#include "ColaError.h"
#include <string>
#include <iostream>
#include <fstream>

using namespace std;
int iteradorError=0;
int iteradorNombreError=0;
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

void ColaError::generarImagen(){
    iteradorError++;
    string iterador = to_string(iteradorError);
    string nombre = "colaerror"+iterador;
    ofstream fs(nombre+".dot");
        fs<<"digraph G {"<<"\n"<<endl;
        fs << "rankdir = UD;\n" <<endl;
        fs << "\tnode [shape=record,color=black];" <<endl;
        fs << "label = \"Cola de Error\"; \n"<<endl;
        fs << "color= black \n"<<endl;
    NodoCola* actual = this->frente;

    while(actual!=NULL){
        iteradorNombreError++;
        fs<<"\t\tN_"<<iteradorNombreError<<"[label = \"ID: "<<actual->id<<"\\nTipo : "<<actual->tipo<<"\\nDescripcion: "<<actual->descripcion<<"\"];\n"<<endl;
        actual = actual->siguiente;

    }
    for(int i=1;i<iteradorNombreError;i++){
        fs<<"N_"<<i<<"->"<<"N_"<<i+1<<";"<<endl;
        fs<<"N_"<<i+1<<"->"<<"N_"<<i<<";"<<endl;

    }
    fs << " }" << endl;
    fs.close();
    string info = "dot -Tsvg "+nombre+".dot -o "+nombre+".svg";
    const char* c = info.c_str();
    cout << c;
    cout << "\n     *Generado exitosamente"<<endl;
    system(c);
}
ColaError::~ColaError()
{
    //dtor
}
