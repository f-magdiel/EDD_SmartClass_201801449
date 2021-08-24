#include <iostream>
#include "Menu.h"
#include <string>
#include "Archivo.h"
#include "ColaError.h"
#include "ListaDobleCircular.h"
#include "ArchivoTarea.h"
#include "Matriz.h"
#include "ListaDoble.h"

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

cout << "   -Ingrese una opcion >> ";
getline(cin,opcionPrincipal);

//opciones del menu
if(opcionPrincipal == "1"){
    leerArchivo();
    colaDeError.mostrarError();
    colaDeError.mostrarCola();
    cout << "\n" << endl;
    menuPrincipal();
}else if(opcionPrincipal == "2"){
    archivoTarea.leerArchivoTarea();
    linealizacion();
    colaDeError.mostrarCola();
    //listadoble.imprimir();
    menuPrincipal();

}else if(opcionPrincipal == "3"){
    ingresoManual();
}else if(opcionPrincipal == "4"){
 cout << "Reportes" << endl;
}else if(opcionPrincipal == "5"){
 exit(0);
}else{

    cout << "   *ERROR: Al menos seleccione una opcion" << endl;
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

    cout << "-Ingrese una opcion >> ";
    getline(cin,opcionOperaciones);

    if(opcionOperaciones == "1"){
        operacionEstudiantes();
    }else if(opcionOperaciones == "2"){
        operacionTareas();
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
            cout << "   -Ingrese carnet >> ";
            getline(cin,_carnet);
            cout <<"\n";
            cout << "   -Ingrese DPI >> ";
            getline(cin,_dpi);
            cout <<"\n";
            cout << "   -Ingrese nombre >> ";
            getline(cin,_nombre);
            cout <<"\n";
            cout << "   -Ingrese carrera >> ";
            getline(cin,_carrera);
            cout <<"\n";
            cout << "   -Ingrese password >> ";
            getline(cin,_pass);
            cout <<"\n";
            cout << "   -Ingrese creditos >> ";
            getline(cin,_creditos);
            cout <<"\n";
            cout << "   -Ingrese correo >> ";
            getline(cin,_correo);
            cout <<"\n";
            informacion = _carnet+","+_dpi+","+_nombre+","+_carrera+","+_pass+","+_creditos+","+_edad+","+_correo;

            validacionCadena(informacion);
            colaDeError.mostrarCola();
            listadc.mostrar();
            colaDeError.mostrarCola();
            operacionEstudiantes();
        }else if(opEstudiante == "2"){
            cout << "   -Ingrese el dpi >> ";
            getline(cin,_dpi);
            listadc.buscarModificar(_dpi);
            listadc.mostrar();
        }else if(opEstudiante == "3"){
            cout << "   -Ingrese el dpi >> ";
            getline(cin,_dpi);
            listadc.eliminar(_dpi);
            listadc.mostrar();
            operacionEstudiantes();
        }else if(opEstudiante == "4"){
            ingresoManual();
        }else{
            cout << "   *Ingrese una opcion valida" << endl;
            operacionEstudiantes();
        }

}

void operacionTareas(){
        string opTareas;
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
        printf("%c          TAREAS           %c\n",186,186);
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
        printf("\n");
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c \n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
        printf("%c  [1] Agregar una Tarea    %c\n",186,186);
        printf("%c  [2] Modificar una Tarea  %c\n",186,186);
        printf("%c  [3] Eliminar una Tarea   %c\n",186,186);
        printf("%c  [4] Regresar             %c\n",186,186);
        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
        cout << "\n";
        cout << "  -Ingrese una opcion >> ";
        getline(cin,opTareas);
}
void linealizacion(){
    int id_;
    string carnet_;
    string nombre_;
    string descripcion_;
    string materia_;
    string fecha_;
    string hora_;
    string estado_;
    int linea_;

    for(int i=0;i<30;i++){
        for (int j=0;j<9;j++){
            for(int k=0;k<5;k++){
                id_ = matrizTareas[k][j][i]->id;
                carnet_ = matrizTareas[k][j][i]->carnet;
                nombre_ = matrizTareas[k][j][i]->nombreTarea;
                descripcion_ = matrizTareas[k][j][i]->descripcion;
                materia_ = matrizTareas[k][j][i]->materia;
                fecha_ = matrizTareas[k][j][i]->fecha;
                hora_ = matrizTareas[k][j][i]->hora;
                estado_ = matrizTareas[k][j][i]->estado;
                linea_ = matrizTareas[k][j][i]->k;
                listadoble.agregar(id_,carnet_,nombre_,descripcion_,materia_,fecha_,hora_,estado_,linea_);
            }
        }
    }
}


