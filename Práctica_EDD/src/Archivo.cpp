#include "Archivo.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <stdlib.h>
#include <regex>
#include "ListaDobleCircular.h"
#include "ColaError.h"

using namespace std;
void leerArchivo(){
    string ruta;
    string lineas;
    string texto = "";
    int contadorEntrada = 0;
cout << "   -Ingrese la ruta del archivo >> ";
getline(cin,ruta);

    ifstream archivo;
    archivo.open(ruta,ios::in);
    if(archivo.fail()){
        cout << "   *No se pudo abrir el archivo" << endl;
    }else{
        while(!archivo.eof()){
            getline(archivo,lineas); //lee cada linea
            contadorEntrada++;
            if(contadorEntrada > 1){
                validacionCadena(lineas);
            }

        }
    }
    archivo.close();

}
void validacionCadena(string lineas){
    //cout << "lineas > "+lineas << endl;
    vector <string> palabras;
    palabras = split(lineas); //método para hacer split y guardarlo en un arreglo
    bool banderaDPI = false;
    bool banderaCarne = false;
    bool banderaCorreo = false;


    const regex expCorreo ("[a-z0-9_.]+\\@[a-z]+\\.[com|es|org]+");
    string correo = palabras[7];
    //validacion DPI
    if(palabras[1].length() == 13){
        banderaDPI = true;

    }else{
        banderaDPI = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Estudiante","DPI incorrecto",palabras[1]);
    }

   //validación Carnet
   if(palabras[0].length()== 9){
        banderaCarne = true;

   }else{
       banderaCarne = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Estudiante","Carnet incorrecto",palabras[1]);
   }

   //validacion Correo
    banderaCorreo = regex_match(correo,expCorreo);
    if(banderaCorreo){
        banderaCorreo = true;

    }else{
        banderaCorreo = false;
        colaDeError.contadorID++;
        colaDeError.encolar(colaDeError.contadorID,"Estudiante","Correo incorrecto",palabras[1]);
    }
    //validacion paso a paso

    //validacion de entradas y almacenamiento
    if((banderaDPI == true)&&(banderaCarne == true)&&(banderaCorreo==true)){
        //para lista doble circular, sin errores
        listadc.agregarFinal(palabras[0],palabras[1],palabras[2],palabras[3],palabras[4],palabras[5],palabras[6],palabras[7]);

    }else{
        //lista doble con errores, pero se auxilia de la cola de errores
        listadc.agregarFinal(palabras[0],palabras[1],palabras[2],palabras[3],palabras[4],palabras[5],palabras[6],palabras[7]);

    }

}

vector<string> split(string linea) {

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


