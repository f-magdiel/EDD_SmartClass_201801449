#include "ListaDobleCircular.h"
#include <string>
#include <iostream>
#include "ColaError.h"
#include "Menu.h"

using namespace std;
ListaDobleCircular::ListaDobleCircular()
{
    this->cabeza = NULL;
    this->cola = NULL;
}

void ListaDobleCircular::agregarFinal(string _carnet,string _dpi, string _nombre, string _carrera, string _pass,string _creditos, string _edad, string _correo){

    NodoDobleCircular* nuevoNodo = new NodoDobleCircular(_carnet,_dpi,_nombre,_carrera,_pass,_creditos,_edad,_correo);
    NodoDobleCircular* actual = this->cabeza;
    if(this->cabeza == NULL){
       this->cabeza = nuevoNodo;
       this->cola = nuevoNodo;
       nuevoNodo->siguiente = this->cabeza;
       this->cabeza->anterior = nuevoNodo;
       nuevoNodo->anterior = actual;
    }else{
        while(actual->siguiente!=this->cabeza){
            actual = actual->siguiente;
        }
        actual->siguiente = nuevoNodo;
        nuevoNodo->siguiente = this->cabeza;
        this->cola = nuevoNodo;
        this->cabeza->anterior = nuevoNodo;
        nuevoNodo->anterior = actual;
    }
}

void ListaDobleCircular::agregarInicio(string _carnet,string _dpi, string _nombre, string _carrera,string _pass, string _creditos, string _edad, string _correo){

    NodoDobleCircular* nuevoNodo = new NodoDobleCircular(_carnet,_dpi,_nombre,_carrera,_pass,_creditos,_edad,_correo);
    if(this->cabeza == NULL){
        this->cabeza = nuevoNodo;
        this->cola = nuevoNodo;
        nuevoNodo->siguiente = this->cabeza;
        nuevoNodo->anterior = this->cola;

    }else{
        nuevoNodo->siguiente = this->cabeza;
        this->cabeza->anterior = nuevoNodo;
        this->cabeza = nuevoNodo;
        nuevoNodo->anterior = this->cola;
        this->cola->siguiente = this->cabeza;
    }
}

void ListaDobleCircular::buscarModificar(string _dpi){
    string informacion="";
    string datoACambiar;

    string opcion;

    NodoDobleCircular* actual = this->cabeza;
    do{
        if(_dpi == actual->dpi){
            informacion = actual->carnet+","+actual->dpi+","+actual->nombre+","+actual->carrera+","+actual->password+","+actual->creditos+","+actual->edad+","+actual->correo;
            cout << "   -Datos encontrados: "+informacion << endl;
            cout << "Escoger dato a modificar: "<<endl;
            cout << "1. Carnet" << endl;
            cout << "2. DPI" << endl;
            cout << "3. Nombre <<" <<endl;
            cout << "4. Carrera"<< endl;
            cout << "5. Pass" << endl;
            cout << "6. Creditos" << endl;
            cout << "7. Edad" << endl;
            cout << "8. Correo" << endl;
            cout << "9. Regresar" << endl;
            getline(cin,opcion);

            if(opcion == "1"){
             cout << "  -Ingrese el carnet:";
             getline(cin,datoACambiar);
             actual->carnet=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Carnet actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "2"){
             cout << "  -Ingrese el DPI: ";
             getline(cin,datoACambiar);
             actual->dpi=datoACambiar;
             colaDeError.cima(_dpi);
             cout << "   -DPI actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "3"){
            cout << "  -Ingrese el nombre:";
             getline(cin,datoACambiar);
             actual->nombre=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Nombre actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "4"){
             cout << "  -Ingrese la carrera:";
             getline(cin,datoACambiar);
             actual->carrera=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Carrera actualizada" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "5"){
             cout << "  -Ingrese el password:";
             getline(cin,datoACambiar);
             actual->password=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Password actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "6"){
             cout << "  -Ingrese los creditos:";
             getline(cin,datoACambiar);
             actual->creditos=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Creditos actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "7"){
             cout << "  -Ingrese la edad:";
             getline(cin,datoACambiar);
             actual->edad=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Edad actualizada" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "8"){
             cout << "  -Ingrese el correo:";
             getline(cin,datoACambiar);
             actual->correo=datoACambiar;
             colaDeError.cima(_dpi);
             cout <<"   -Correo actualizado" << endl;
             datoACambiar = "";
             colaDeError.mostrarCola();
             listadc.mostrar();
             buscarModificar(_dpi);
             break;

            }else if(opcion == "9"){
                operacionEstudiantes();
                break;
            }else{
                buscarModificar(_dpi);
                break;
            }

        }
        actual = actual->siguiente;
    }while(actual!=this->cabeza);

    if(informacion==""){
        cout << "Dato no encotrado, por favor ingresar un dato valido" << endl;
        operacionEstudiantes();
    }

}

void ListaDobleCircular::eliminar(string _dpi){

    NodoDobleCircular* actual = this->cabeza;
    NodoDobleCircular* valorAnterior = NULL;
    NodoDobleCircular* valorMuySiguiente = NULL;
    bool encontrado = false;

    while((actual!=NULL) && (encontrado == false)){
        encontrado = (actual->dpi == _dpi);
        if(encontrado==false){
            valorAnterior = actual;
            actual = actual->siguiente;
        }
    }

    if(actual!=NULL){
        if(actual == this->cabeza){
            this->cabeza = actual->siguiente;
            this->cabeza->anterior = this->cola;
            this->cola->siguiente = this->cabeza;
        }else if(actual == this->cola){
            this->cola = valorAnterior;
            this->cola->siguiente = this->cabeza;
            this->cabeza->anterior = this->cola;
        }else{
            valorMuySiguiente = actual->siguiente;
            valorAnterior->siguiente = actual->siguiente;
            valorMuySiguiente->anterior = valorAnterior;
        }


    }
    cout << "   Se elimino el dato" << endl;
}

void ListaDobleCircular::mostrar(){
    cout << "*******Mostrar********" << endl;
    string resultado ="";
    NodoDobleCircular* actual = this->cabeza;
    do{
        resultado+= actual->carnet+","+actual->dpi+","+actual->nombre+","+actual->carrera+","+actual->password+","+actual->creditos+","+actual->edad+","+actual->correo+"\n";
        actual = actual->siguiente;
    }while(actual!=this->cabeza);

    //delete(actual);
    cout << resultado;
}

ListaDobleCircular::~ListaDobleCircular()
{
    //dtor
}
