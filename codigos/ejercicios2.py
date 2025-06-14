# CREAR UN JUEGO DE FUSIÓN
# El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar para formar personajes más poderosos que tengan más poder...
# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusiones. salga un nuevo personaje con habilidades mejoradas.
# Una posible formula es: El promedio de las habilidades de ambos, ¡al cuadrado!

class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}. Velocidad{self.velocidad})"
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**1.3
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**1.3
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
goku = Personaje("Goku",1000,1000)
vegeta = Personaje("Vegeta",1999,1999)
goten = Personaje("Goten",250,300)
trunks = Personaje("Trunks",300,250)

gogeta = goku + vegeta
gotenks = goten + trunks
goteka = gogeta + gotenks
print(gogeta)
print(gotenks)
print(goteka)