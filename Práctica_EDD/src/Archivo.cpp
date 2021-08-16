#include "Archivo.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
void leerArchivo(){
    string ruta;
    string lineas;
    string texto = "";
cout << "   Ingrese la ruta del archivo >> ";
getline(cin,ruta);

    ifstream archivo;
    archivo.open(ruta,ios::in);
    if(archivo.fail()){
        cout << "No se pudo abrir el archivo" << endl;
    }else{
        while(!archivo.eof()){
            getline(archivo,lineas);
            lineas = lineas + "\n";
            texto += lineas;
        }
    }
    cout << texto << endl;
    archivo.close();
}
