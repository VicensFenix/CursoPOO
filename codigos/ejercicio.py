# Tiene que tener una clase llamada Estudiante, con los atributos: Nombre, edad y grado. Tiene que tener un método llamado estudiar y que diga el estudiante(nombre está estudiando). Se debe interactuar con el usuario y este debe briandar los atirbutos. Al escribir "estudiar" utiliza el método estudiar

class Estudiante:
    def __init__(self,nombre, edad, grado):
        self.nombre = nombre
        self.grado = grado
        self.edad = edad
        
    def estudiar(self):
        print("Estudiando...")
        
nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")  
grado = input("Digame su grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f""""
        DATOS DEL ESTUDIANTE: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
