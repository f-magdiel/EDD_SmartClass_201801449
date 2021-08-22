#include "ArchivoTarea.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <stdlib.h>
#include <regex>

using namespace std;
ArchivoTarea::ArchivoTarea()
{

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
                cout << lineas << endl;
            }

        }
    }
}



ArchivoTarea::~ArchivoTarea()
{
    //dtor
}
