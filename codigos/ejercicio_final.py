# Importamos el pipeline de análisis de emociones
from transformers import pipeline

# Cargamos el modelo de emociones de Hugging Face
analizador = pipeline("text-classification", model='j-hartmann/emotion-english-distilroberta-base', return_all_scores=False)

def detectar_emocion(texto_usuario):
    """
    Analiza el texto ingresado por el usuario y revela la emoción dominante.
    """
    resultado = analizador(texto_usuario)
    return resultado[0]["label"], resultado[0]["score"]

# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Ingrese un texto para detectar la emoción: ") 
    emocion, puntaje = detectar_emocion(texto)
    print(f"La emoción detectada fue: {emocion} con un puntaje de {puntaje*100:.2f}%")
