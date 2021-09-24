from analizador.sintactico import parser

if __name__ == '__main__':
    path = "C:\\Users\\Magdiel\\Desktop\\Archivos de prueba\\Estudiantes.txt"
    f = open(path,"r", encoding="utf-8")
    mensaje = f.read()
    f.close()
    
    resultado_analisis= parser.parse(mensaje)

    for item in resultado_analisis:
        print(item["type"])
        for at in item["atributos"]:
            print(at)
