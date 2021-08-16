#include <iostream>
#include "Menu.h"
#include <string>
#include "Archivo.h"
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

cout << "Ingrese una opcion >> ";
getline(cin,opcionPrincipal);

//opciones del menu
if(opcionPrincipal == "1"){
leerArchivo();

}else if(opcionPrincipal == "2"){
 cout << "Carga de tareas" << endl;
}else if(opcionPrincipal == "3"){
 cout << "Ingreso manual" << endl;
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


