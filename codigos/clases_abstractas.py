from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando de: {self.actividad}")
        
dalto = Estudiante("Lucas", 21, "Masculino", "Programación")
dalto.presentarse()  
dalto.hacer_actividad()    

vicente = Estudiante("Vicente", 18, "Masculino", "Programación")
vicente.presentarse()  
vicente.hacer_actividad()    