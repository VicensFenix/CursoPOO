class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    # Devuelve una representación del objeto en una cadena de texto 
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    # Se usa para definir cómo debería mostrarse una instancia de una clase cuando se la representa como una cadena
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    # Se usa para agregar un nuevo valor y sumarlo
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)
    
dalto = Persona("Lucas",21)
paco = Persona("Paco",30)
maria = Persona("Maria",18)

# Sobre carga de operadores
nueva_persona = dalto + paco + maria
print(nueva_persona.nombre)
