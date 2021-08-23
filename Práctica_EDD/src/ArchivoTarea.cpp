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

using namespace std;
int contadorIDTarea=0;
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

    if(hora>=0 && hora<=8){
        validacionTarea(mes,dia,hora,palabrasTarea[3],palabrasTarea[4],palabrasTarea[5],palabrasTarea[6],palabrasTarea[7],palabrasTarea[8]);
    }else{
        cout << "Hora valio" <<endl;
        cout << hora;
    }


}

void ArchivoTarea::validacionTarea(int _mes,int _dia,int _hora,string _carnet,string _nombreTarea,string _descripcion,string _materia ,string _fecha,string _estado){
    //validacion de datos
    bool banderaFecha=false;
    bool banderaCarnet=false;
    bool banderaHora=false;
    string hora_ = to_string(_hora);

    const regex expFecha ("\\d{4}\\/([[0][7|8|9]|[1][0|1])\\/([[0][1-9]|[1][0-9]|[2][0-9]|[3][0])");
    //validacion carnet
    banderaCarnet = listadc.buscar(_carnet);
    cout << "POsiciones" << endl;
    cout << "Mes: ";
    cout << _mes;
    cout << " Dia: ";
    cout << _dia;
    cout << " Hora: ";
    cout << _hora << endl;
    //validacion carnet
    if(banderaCarnet==true){
        banderaCarnet = true;

    }else{
        banderaCarnet = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Carnet no encontrado",_carnet);
    }

    //validacion fecha
    banderaFecha = regex_match(_fecha,expFecha);
    if(banderaFecha){
        banderaFecha = true;
    }else{
        banderaFecha = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Fecha incorrecta",_carnet);
    }

    //validacion hora
    if(_hora>=8 && _hora<=16){
        banderaHora = true;
    }else{
        banderaHora = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Tarea","Hora incorrecta",_carnet);
    }

    //validacion ingreso datos
    if((banderaCarnet == true)&&(banderaFecha == true)&&(banderaHora == true)){
        contadorIDTarea++;
        matrizTareas[_mes][_hora][_dia] ->insertar(contadorIDTarea,hora_,_carnet,_nombreTarea,_descripcion,_materia,_fecha,_estado);

    }else{
        contadorIDTarea++;
        matrizTareas[_mes][_hora][_dia] ->insertar(contadorIDTarea,hora_,_carnet,_nombreTarea,_descripcion,_materia,_fecha,_estado);

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

ArchivoTarea::~ArchivoTarea()
{
    //dtor
}
