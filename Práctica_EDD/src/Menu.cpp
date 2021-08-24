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
    colaDeError.mostrarCola();
    listadoble.imprimir();
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
            string op;
            cout << "   *Estas seguro de eliminar ese dato [S/N] >> ";
            getline(cin,op);
            if(op=="S"){
                listadc.eliminar(_dpi);
                listadc.mostrar();
                operacionEstudiantes();
            }else{
                operacionEstudiantes();
            }
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

        string mes,dia,hora,carnet,nombre,descripcion,materia,fecha,estado;
        string informacionTarea;
        if(opTareas=="1"){
            cout << "-INGRESO TAREA"<<endl;
            cout << "   -Ingrese mes >> ";
            getline(cin,mes);
            cout << "\n";

            cout << "   -Ingrese dia >> ";
            getline(cin,dia);
            cout << "\n";

            cout << "   -Ingrese hora >> ";
            getline(cin,hora);
            cout << "\n";

            cout << "   -Ingrese carnet >> ";
            getline(cin,carnet);
            cout << "\n";

            cout << "   -Ingrese nombre >> ";
            getline(cin,nombre);
            cout << "\n";

            cout << "   -Ingrese descripcion >> ";
            getline(cin,descripcion);
            cout << "\n";

            cout << "   -Ingrese materia >> ";
            getline(cin,materia);
            cout << "\n";

            cout << "   -Ingrese fecha >> ";
            getline(cin,fecha);
            cout << "\n";

            cout << "   -Ingrese estado >> ";
            getline(cin,estado);
            cout <<"\n";
            informacionTarea = mes+","+dia+","+hora+","+carnet+","+nombre+","+descripcion+","+materia+","+fecha+","+estado;
            archivoTarea.dividirCadena(informacionTarea);
            operacionTareas();
        }else if(opTareas=="2"){
            int cara,fila,columna;
            string _cara,_fila,_columna;

            cout << "MODIFICAR"<<endl;
            cout << "   -Ingrese cara >> ";
            getline(cin,_cara);
            cout << "   -Ingrese fila >> ";
            getline(cin,_fila);
            cout << "   -Ingrese columna >> ";
            getline(cin,_columna);
            cara = stoi(_cara);
            fila = stoi(_fila);
            columna = stoi(_columna);
            modificacionMatriz(cara,fila,columna);
            operacionTareas();
        }else if(opTareas=="3"){
            int TZ = 5; //caras
            int TJ = 9;
            int _k=0;

            int cara,fila,columna;
            string _cara,_fila,_columna;
            string eliminacion;
            cout << "ELIMINAR"<<endl;
            cout << "   -Ingrese cara >> ";
            getline(cin,_cara);
            cout << "   -Ingrese fila >> ";
            getline(cin,_fila);
            cout << "   -Ingrese columna >> ";
            getline(cin,_columna);
            cara = stoi(_cara);
            fila = stoi(_fila);
            columna = stoi(_columna);
            _k = (columna*TJ+fila)*TZ+cara;

            cout << "   *Estas seguro de eliminar esa posicion[S/N] >> ";
            getline(cin,eliminacion);
            if(eliminacion == "S"){
                matrizTareas[cara][fila][columna]->insertar(-1,"-1","-1","-1","-1","-1","-1","-1");
                listadoble.buscarAgregar(-1,"-1","-1","-1","-1","-1","-1","-1",_k);
                listadoble.imprimir();
                operacionTareas();
            }else{
                operacionTareas();
            }

        }else if(opTareas=="4"){
            ingresoManual();
        }else{
            cout << "   *Ingrese una opcion valida" << endl;
            operacionTareas();
        }
}


void modificacionMatriz(int cara,int fila, int columna){
    if(matrizTareas[cara][fila][columna]->id!= -1){

            string op;
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
            printf("%c      MODIFICAR     %c\n",186,186);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
            printf("%c  [1] Carnet        %c\n",186,186);
            printf("%c  [2] Nombre Tarea  %c\n",186,186);
            printf("%c  [3] Descripcion   %c\n",186,186);
            printf("%c  [4] Materia       %c\n",186,186);
            printf("%c  [5] Fecha         %c\n",186,186);
            printf("%c  [6] Hora          %c\n",186,186);
            printf("%c  [7] Estado        %c\n",186,186);
            printf("%c  [8] Regresar      %c\n",186,186);
            printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
            cout << "   -Ingrese una opcion >> ";
            getline(cin,op);

            string datos;
            string _carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado;
            int _linea;

            //condiciones del menu
            if(op=="1"){
                cout << "   -Ingrese carnet >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->carnet = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="2"){
                cout << "   -Ingrese nombre tarea >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->nombreTarea = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="3"){
                cout << "   -Ingrese descripcion >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->descripcion = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="4"){
                cout << "   -Ingrese materia >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->materia = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="5"){
                cout << "   -Ingrese fecha >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->fecha = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="6"){
                cout << "   -Ingrese hora >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->hora = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="7"){
                cout << "   -Ingrese estado >> ";
                getline(cin,datos);
                matrizTareas[cara][fila][columna]->estado = datos;

                _carnet = matrizTareas[cara][fila][columna]->carnet;
                _nombre = matrizTareas[cara][fila][columna]->nombreTarea;
                _descripcion = matrizTareas[cara][fila][columna]->descripcion;
                _materia = matrizTareas[cara][fila][columna]->materia;
                _fecha = matrizTareas[cara][fila][columna]->fecha;
                _hora = matrizTareas[cara][fila][columna]->hora;
                _estado = matrizTareas[cara][fila][columna]->estado;
                _linea = matrizTareas[cara][fila][columna]->k;

                listadoble.actualizar(_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado,_linea);

                cout << "\n";
            }else if(op=="8"){
                operacionTareas();
            }else{
                modificacionMatriz(cara,fila,columna);
                cout << "   *Ingrese una opcion valida"<<endl;
            }
    }else{
            cout << "   *Posicion vacia" << endl;
            operacionTareas();
    }
}


