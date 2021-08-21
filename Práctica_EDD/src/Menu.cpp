#include <iostream>
#include "Menu.h"
#include <string>
#include "Archivo.h"
#include "ColaError.h"

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
cout << "\n";
int opcionOperaciones=0;
    do{
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
    cin>>opcionOperaciones;

    if(opcionOperaciones == 1){
        cout << "Estudiantes";
        cout << "\n";
    }else if(opcionOperaciones == 2){
        cout << "Tareas";
    }else if(opcionOperaciones == 3){
        menuPrincipal();
    }else{
        cout << "   *Ingrese una opcion valida" << endl;
    }
    } while(opcionOperaciones!=4);
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



