import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Configuración de la API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("No se encontró la clave de API de Gemini. Por favor, configura GEMINI_API_KEY en tu archivo .env")

genai.configure(api_key=API_KEY)

class Asistente:
    def __init__(self):
        # Configuración de generación
        self.history = []
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Crear el modelo
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
            system_instruction="eres un asistente de propósito general. Siempre respondes como si fueras un pirata",
        )


    def iniciar_sesion(self):
        """
        Iniciar o reiniciar explícitamente la sesión de chat
        
        Args:
            history (list, optional): Historial de conversación para iniciar. 
                                      Si no se proporciona, inicia con historial vacío.
        
        Returns:
            Chat session
        """
        
        # Iniciar nueva sesión de chat
        self.chat_session = self.model.start_chat(history=self.history)
        return self.chat_session

    def start_chat(self):
        """
        Iniciar una nueva sesión de chat con historial opcional
        
        Args:
            history (list, optional): Historial de conversación previo. 
                                      Si no se proporciona, usa el historial actual.
        
        Returns:
            Chat session
        """
        if history is None:
            history = self.history
        return self.model.start_chat(history=history)

    def send_message(self, message):
        """
        Enviar un mensaje y obtener respuesta
        
        Args:
            message (str): Mensaje a enviar
        
        Returns:
            str: Respuesta del modelo
        """
        # Agregar mensaje del usuario al historial
        self.history.append({
            "role": "user",
            "content": message
        })
        
        # Enviar mensaje a través de la sesión de chat actual
        response = self.chat_session.send_message(message)
        
        # Agregar respuesta del modelo al historial
        self.history.append({
            "role": "model", 
            "content": response.text
        })
        
        return response.text

    def reset_chat(self):
        """
        Reiniciar la sesión de chat con historial vacío
        """
        self.chat_session = self.model.start_chat(history=[])
