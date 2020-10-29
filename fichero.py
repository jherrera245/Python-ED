from datetime import datetime

class Fichero:
    def __init__(self):
        self.__now = None
        self.__file = "informacion.txt"

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
