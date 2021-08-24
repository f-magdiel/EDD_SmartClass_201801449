#include "ArchivoTarea.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <stdlib.h>
#include <regex>
#include "ListaDobleCircular.h"
#include "Matriz.h"
#include "ColaError.h"
#include "ListaDoble.h"

using namespace std;
int contadorIDTarea=0;
int contadorErrorTarea = 0;
ArchivoTarea::ArchivoTarea()
{
    this->contadorID =0;
}

void ArchivoTarea::leerArchivoTarea(){
    string lineas;
    string ruta;
    string texto;
    int contadorEntrada =0;
    cout << "   -Ingrese la ruta del archivo >> ";
    getline(cin,ruta);

    ifstream archivo;
    archivo.open(ruta,ios::in);
    if(archivo.fail()){
        cout << "   *No se pudo abrir el archivo" << endl;
    }else{
        while(!archivo.eof()){
            getline(archivo,lineas);//lee cada linea del archivo
            contadorEntrada++;
            if(contadorEntrada > 1){
            dividirCadena(lineas);
            }

        }
    }
    archivo.close();
    verError();
}

void ArchivoTarea::dividirCadena(string lineas){
    int mes;
    int dia;
    int hora;
    vector <string> palabrasTarea;
    palabrasTarea = splitTarea(lineas); //método para hacer split y guardarlo en un arreglo
    mes = stoi(palabrasTarea[0]);
    dia = stoi(palabrasTarea[1]);
    hora = stoi(palabrasTarea[2]);
    mes = mes-7;
    dia = dia-1;
    hora = hora-8;
    //validacion de posiciones en la matriz
    if(hora>=0 && hora<=8){
        if(dia>=0 && dia<=29){
            if(mes>=0 && mes<=4){
                    //para validar solo una tarea en una hora
                string dato = matrizTareas[mes][hora][dia]->carnet;
                if(dato=="-1"){
                   validacionTarea(mes,dia,hora,palabrasTarea[3],palabrasTarea[4],palabrasTarea[5],palabrasTarea[6],palabrasTarea[7],palabrasTarea[8]);
                }else{
                cout << "   *Posicion Ocupada"<<endl;
                }

            }
        }
    }


}

void ArchivoTarea::validacionTarea(int _mes,int _dia,int _hora,string _carnet,string _nombreTarea,string _descripcion,string _materia ,string _fecha,string _estado){
    //validacion de datos
    bool banderaFecha=false;
    bool banderaCarnet=false;
    bool banderaHora=false;
    int TZ = 5; //caras
    int TJ = 9;
    int _k=0;

    _k = (_dia*TJ+_hora)*TZ+_mes;
    string hora_ = to_string(_hora);

    const regex expFecha ("\\d{4}\\/([[0][7|8|9]|[1][0|1])\\/([[0][1-9]|[1][0-9]|[2][0-9]|[3][0])");
    //validacion carnet
    banderaCarnet = listadc.buscar(_carnet);

    //validacion carnet
    if(banderaCarnet==true){
        banderaCarnet = true;

    }else{
        contadorErrorTarea++;
        banderaCarnet = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Carnet no encontrado",_carnet);
    }

    //validacion fecha
    banderaFecha = regex_match(_fecha,expFecha);
    if(banderaFecha){
        banderaFecha = true;
    }else{
        contadorErrorTarea++;
        banderaFecha = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Fecha incorrecta",_carnet);
    }

    //validacion hora
    if(_hora>=0 && _hora<=8){
        banderaHora = true;
    }else{
        contadorErrorTarea++;
        banderaHora = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Hora incorrecta",_carnet);
    }

    //validacion ingreso datos
    if((banderaCarnet == true)&&(banderaFecha == true)&&(banderaHora == true)){
        contadorIDTarea++;
        matrizTareas[_mes][_hora][_dia] ->insertar(contadorIDTarea,hora_,_carnet,_nombreTarea,_descripcion,_materia,_fecha,_estado);
        listadoble.buscarAgregar(contadorIDTarea,_carnet,_nombreTarea,_descripcion,_materia,_fecha,hora_,_estado,_k);
    }else{
        contadorIDTarea++;
        matrizTareas[_mes][_hora][_dia] ->insertar(contadorIDTarea,hora_,_carnet,_nombreTarea,_descripcion,_materia,_fecha,_estado);
        listadoble.buscarAgregar(contadorIDTarea,_carnet,_nombreTarea,_descripcion,_materia,_fecha,hora_,_estado,_k);
    }



}

vector<string> splitTarea(string linea) {

    int posInit = 0;
    string separador = ",";
    int posFound = 0;
    string separado;
    vector<string> resultado;

    while(posFound >= 0){
        posFound = linea.find(separador, posInit);
        separado = linea.substr(posInit, posFound - posInit);
        posInit = posFound + 1;
        resultado.push_back(separado);
    }

    return resultado;
}

void ArchivoTarea::verError(){
    if(contadorErrorTarea!=0){
        cout << "   *Error encontrado: ";
        cout << contadorErrorTarea << endl;
    }else{
        cout << "   *Error encontrado: ";
        cout << contadorErrorTarea << endl;
    }
}

ArchivoTarea::~ArchivoTarea()
{
    //dtor
}
