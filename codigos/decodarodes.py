def decorador(funcion):
    def fucion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return fucion_modificada()

def saludo():
    print("Hola Dalto")
    
saludo_modificado = decorador(saludo)
saludo_modificado()