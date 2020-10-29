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

    #Agregar nuevo contenido al archivo
    def __sobreEscribirArchivo(self, cadena):
        with open(self.__file, "a") as fh:
            fh.write("Contendio: {}\n".format(cadena))
            fh.write("Fecha de Modificación: {}\n".format(self.__getFechaModificacion()))
            fh.write("Hora de Modificación: {}\n\n".format(self.__getHoraModificacion()))
            fh.close()
        print("Archivo modificado con exito!!!\n")

    #Metodo para obtener la fecha actual en python
    def __getFechaModificacion(self):
        self.__now = datetime.now()
        return str(self.__now.day)+"/"+str(self.__now.month)+"/"+str(self.__now.year)

    #Metodo para obtener la fecha actual en python 
    def __getHoraModificacion(self):
        self.__now = datetime.now()
        return str(self.__now.hour)+":"+str(self.__now.minute)+":"+str(self.__now.second)

archivo = Fichero()
while True:
    try:
        print("Menu de Opciones")
        print("1) Escrbir en el archivo")
        print("2) Mostrar el Contenido del archivo")
        print("3) Salir")

        opcion = int(input("\nSelecciona una de las opciones: "))
        if opcion == 1:
            archivo.escribirEnArchivo()
        elif opcion == 2:
            archivo.leerArchivo()
        elif opcion == 3:
            print("Adios !!!")
            break
        else:
            print("La entrada no corresponde a una opción valida!!\n") 
    except ValueError as e:
        print("Por favor ingrese unicamente numeros\n")