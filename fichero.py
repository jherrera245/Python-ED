from datetime import datetime

class Fichero:
    def __init__(self):
        self.__now = None
        self.__file = "informacion.txt"

    #Leer informacion del archivo
    def leerArchivo(self):
        data = open(self.__file, "r") #Leer archivos del fichero
        for line in data:
            print(line.rstrip("\n"))
        data.close()

    def escribirEnArchivo(self):
        cadena = input("Escriba el texto a agregar: ")
        self.__sobreEscribirArchivo(cadena)

