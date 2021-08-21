#include <iostream>
#include "Menu.h"
#include <string>
#include "Archivo.h"
#include "ColaError.h"
#include "ListaDobleCircular.h"

using namespace std;
void menuPrincipal(){

    string opcionPrincipal;
printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
printf("%c        MENU PRINCIPAL       %c\n",186,186);
printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
printf("\n");
printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
printf("%c  [1] Carga de Estudiantes   %c\n",186,186);
printf("%c  [2] Carga de Tareas        %c\n",186,186);
printf("%c  [3] Ingreso Manual         %c\n",186,186);
printf("%c  [4] Reportes               %c\n",186,186);
printf("%c  [5] Salir                  %c\n",186,186);
printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);

cout << "-Ingrese una opcion >> ";
getline(cin,opcionPrincipal);

//opciones del menu
if(opcionPrincipal == "1"){
    leerArchivo();
    colaDeError.mostrarError();
    colaDeError.mostrarCola();
    cout << "\n" << endl;
    menuPrincipal();
}else if(opcionPrincipal == "2"){
 cout << "Carga de tareas" << endl;
}else if(opcionPrincipal == "3"){
    ingresoManual();
}else if(opcionPrincipal == "4"){
 cout << "Reportes" << endl;
}else if(opcionPrincipal == "5"){
 exit(0);
}else{

    cout << "ERROR: Al menos seleccione una opcion" << endl;
    cout << "\n" << endl;
    menuPrincipal();
}
}

void ingresoManual(){
    cout << "\n";
    string opcionOperaciones;


    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
    printf("%c            INGRESO MANUAL           %c\n",186,186);
    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
    printf("\n");
    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
    printf("%c  [1] Operaciones Sobre Estudiantes  %c\n",186,186);
    printf("%c  [2] Operaciones Sobre Tareas       %c\n",186,186);
    printf("%c  [3] Regresar                       %c\n",186,186);
    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);

    cout << "-Ingrese una opcion: ";
    getline(cin,opcionOperaciones);

    if(opcionOperaciones == "1"){
        operacionEstudiantes();
    }else if(opcionOperaciones == "2"){
        cout << "Tareas";
    }else if(opcionOperaciones == "3"){
        menuPrincipal();
    }else{
        cout << "   *Ingrese una opcion valida" << endl;
        ingresoManual();
    }

}

void operacionEstudiantes(){
        string opEstudiante;

        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
        printf("%c        ESTUDIANTES            %c\n",186,186);
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
        printf("\n");
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
        printf("%c  [1] Agregar un Estudiante    %c\n",186,186);
        printf("%c  [2] Modificar un Estudiante  %c\n",186,186);
        printf("%c  [3] Eliminar un Estudiante   %c\n",186,186);
        printf("%c  [4] Regresar                 %c\n",186,186);
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
        cout << "\n";
        cout << "  -Ingrese una opcion >> ";
        getline(cin,opEstudiante);

        //variables
        string _carnet,_dpi,_nombre,_carrera,_pass,_creditos,_edad,_correo;
        string informacion;

        if(opEstudiante == "1"){
            cout << "   DATOS A INGRESAR"<< endl;
            cout << "   -Ingrese carnet: ";
            getline(cin,_carnet);
            cout <<"\n";
            cout << "   -Ingrese DPI: ";
            getline(cin,_dpi);
            cout <<"\n";
            cout << "   -Ingrese nombre: ";
            getline(cin,_nombre);
            cout <<"\n";
            cout << "   -Ingrese carrera: ";
            getline(cin,_carrera);
            cout <<"\n";
            cout << "   -Ingrese password: ";
            getline(cin,_pass);
            cout <<"\n";
            cout << "   -Ingrese creditos: ";
            getline(cin,_creditos);
            cout <<"\n";
            cout << "   -Ingrese correo: ";
            getline(cin,_correo);
            cout <<"\n";
            informacion = _carnet+","+_dpi+","+_nombre+","+_carrera+","+_pass+","+_creditos+","+_edad+","+_correo;

            validacionCadena(informacion);
            colaDeError.mostrarCola();
            listadc.mostrar();
            operacionEstudiantes();
        }else if(opEstudiante == "2"){
            cout << "   -Ingrese el dpi: ";
            getline(cin,_dpi);
            listadc.buscarModificar(_dpi);
            listadc.mostrar();
        }else if(opEstudiante == "3"){

        }else if(opEstudiante == "4"){
            ingresoManual();
        }else{
            cout << "   *Ingrese una opcion valida" << endl;
            operacionEstudiantes();
        }

}



