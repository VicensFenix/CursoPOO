# S- SRP, PRINCIPIO DE RESPONSABILIDAD ÚNICO

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion
            
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
# Crear instancia de tanque
tanque = TanqueDeCombustible()
# Crear auto con el tanque
autito = Auto(tanque)

# Mostrar posición inicial
print("Posición inicial:", autito.obtener_posicion())

# Mover auto una distancia (ejemplo: 10)
autito.mover(10)

# Mostrar posición después del movimiento
print("Posición después de moverse:", autito.obtener_posicion())

# Opcional: Mostrar cuánto combustible queda
print("Combustible restante:", tanque.obtener_combustible())