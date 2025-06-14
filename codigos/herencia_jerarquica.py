class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def trabajar(self):
        print("estoy trabajando...")
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,grado,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.grado = grado
        self.universidad = universidad

roberto = Empleado("Roberto",50,"colombiano","Programador",200000)

roberto.trabajar()