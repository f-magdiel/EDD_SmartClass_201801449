#include "Archivo.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <stdlib.h>
#include <regex>

using namespace std;
void leerArchivo(){
    string ruta;
    string lineas;
    string texto = "";
    int contadorEntrada = 0;
cout << "   Ingrese la ruta del archivo >> ";
getline(cin,ruta);

    ifstream archivo;
    archivo.open(ruta,ios::in);
    if(archivo.fail()){
        cout << "No se pudo abrir el archivo" << endl;
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
        cout << "dpi : "+palabras[1]<<endl;
    }else{
        cout << "dpi: invalido" << endl;
    }

   //validación Carne
   if(palabras[0].length()== 9){
        banderaCarne = true;
    cout << "carne : "+palabras[0]<<endl;
   }else{
        cout << "Carne: invalido" << endl;
   }

   //validacion Correo
    banderaCorreo = regex_match(correo,expCorreo);
    if(banderaCorreo){
        cout << "Correo valido"<<endl;
        banderaCorreo = true;
    }else{
    cout << "Correo invalido" << endl;
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


