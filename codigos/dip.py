# D- DIP, PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         # Lógicas para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         # Usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass
    
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras desde el servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        # Usamos el verificador para corregir el texto
        pass
    
corrector = CorrectorOrtografico(Diccionario())