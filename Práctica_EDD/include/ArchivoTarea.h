#ifndef ARCHIVOTAREA_H
#define ARCHIVOTAREA_H
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

class ArchivoTarea
{
    public:
        ArchivoTarea();
        virtual ~ArchivoTarea();

    void leerArchivoTarea();
};

extern ArchivoTarea archivoTarea;

#endif // ARCHIVOTAREA_H
