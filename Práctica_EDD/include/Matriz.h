#ifndef MATRIZ_H
#define MATRIZ_H
#include <string>
#include <iostream>

using namespace std;
class Matriz
{
    public:
        Matriz();
        virtual ~Matriz();
        int k =0;
        int id=0;
        string hora;
        string carnet;
        string nombreTarea;
        string descripcion;
        string materia;
        string fecha;
        string estado;

        void insertar(int,string,string,string,string,string,string,string);
        void mostrarMatriz();
        int getK();
        void setK(int);

};
extern Matriz* matrizTareas [5][9][30];

#endif // MATRIZ_H
