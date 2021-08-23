#ifndef ARCHIVOTAREA_H
#define ARCHIVOTAREA_H
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
vector <string> splitTarea(string);
class ArchivoTarea
{
    public:
        ArchivoTarea();
        virtual ~ArchivoTarea();
    int contadorID =0;
    void leerArchivoTarea();
    void dividirCadena(string);
    void validacionTarea(int,int,int,string,string,string,string,string,string);


};

extern ArchivoTarea archivoTarea;

#endif // ARCHIVOTAREA_H
