# En python como tal no existe el public y privado pero si hay otra forma de llamarlo
# Con un _ al inicio se le indica que es privado
# Con doble __ se indica que nadie puede acceder a el ni el desarrollador
# (privado) _atributo_privado
# (Muy privado) __atributo_privado

class Miclase:
    def __init__(self):
        self.__atributo_privado = "valor"
    
    def __hablar(self):
        print("Hola, como estas")
        
objeto = Miclase()
print(objeto._hablar())