# El getter es para acceder
# El setter es para modificar o establecer

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
        
dalto = Persona("Lucas",21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Lionel")

nombre = dalto.get_nombre()
print(nombre)