# 0- OCP, PRINCIPIO DE ABIERTO/CERRADO

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usario = usuario
        self.mensaje = mensaje
    
    # se utiliza para lanzar una excepción de manera explícita.  
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviendo mail a {self.usario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviendo SMS a {self.usario.sms}")
        
class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviendo SMS a {self.usario.whatsapp}")
        
class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviendo twit a {self.usario.whatsapp}")