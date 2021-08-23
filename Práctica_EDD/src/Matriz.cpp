#include "Matriz.h"

Matriz::Matriz()
{
    this->id = -1;
    this->hora = "-1";
    this->carnet = "-1";
    this->nombreTarea = "-1";
    this->descripcion = "-1";
    this->materia = "-1";
    this->fecha = "-1";
    this->estado = "-1";
}


void Matriz::insertar(int _id,string _hora,string _carnet,string _nombreTarea,string _descripcion,string _materia ,string _fecha,string _estado){
    this->id = _id;
    this->hora = _hora;
    this->carnet = _carnet;
    this->nombreTarea = _nombreTarea;
    this->descripcion = _descripcion;
    this->materia = _materia;
    this->fecha = _fecha;
    this->estado = _estado;
}

void Matriz::mostrarMatriz(){
    int i,j,k;
    for(i=0;i<5;i++){
        for (j = 0;j<9;j++){
            for(k = 0;k<30;k++){

                cout << matrizTareas[i][j][k]->carnet;
                cout << " ";
                cout << "\n";
            }
            cout << "\n";
        }
        cout << "\n";
    }
}

Matriz::~Matriz()
{
    //dtor
}
