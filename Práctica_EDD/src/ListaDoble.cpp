#include "ListaDoble.h"
#include <string>
#include <iostream>
#include <fstream>

using namespace std;
int iteradorNo;
int iteradorNoNombre;
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
        cout << actual->hora;
        cout << " ";
        actual = actual->siguiente;
    }
}

void ListaDoble::generadorImagen(){
    iteradorNo++;
    string iterador = to_string(iteradorNo);
    string nombre = "listalinealizada"+iterador;
    ofstream fs(nombre+".dot");
        fs<<"digraph G {"<<"\n"<<endl;
        fs << "rankdir = LR;\n" <<endl;
        fs << "\tnode [shape=record,color=black];" <<endl;
        fs << "label = \"Lista Tarea Linealizada\"; \n"<<endl;
        fs << "color= black \n"<<endl;
    NodoListaDoble* actual = this->cabeza;

    while(actual!=NULL){
        iteradorNoNombre++;
        fs<<"\t\tN_"<<iteradorNoNombre<<"[label = \"ID: "<<actual->id<<"\\nCarnet : "<<actual->carnet<<"\\nNombre Tares : "<<actual->nombre<<"\\nDescripcion : "<<actual->descripcion<<"\\nMateria : "<<actual->materia<<"\\nFecha : "<<actual->fecha<<"\\nHora : "<<actual->hora<<"\\nEstado: "<<actual->estado<<"\"];\n"<<endl;
        actual = actual->siguiente;

    }

    for(int i=1;i<iteradorNoNombre;i++){
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

ListaDoble::~ListaDoble()
{
    //dtor
}
