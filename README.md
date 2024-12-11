# Proyecto de Integración con Gemini API

## Descripción
Este es un ejemplo básico de cómo integrar la API de Gemini de Google con Python. El proyecto proporciona una estructura inicial que puede ser adaptada para usar con cualquier backend o frontend de tu elección.

## Configuración Inicial

### Requisitos Previos
- Python 3.8+
- Cuenta en Google AI Studio

### Pasos de Instalación

1. **Obtener API Key**:
   - Visita [Google AI Studio](https://aistudio.google.com/)
   - Crea una cuenta o inicia sesión
   - Genera tu API Key para Gemini

2. **Configuración del Entorno**:
   - Renombra ``.env_copy`` a ``.env``
   - Agrega tu API Key en el archivo ``.env``
   ```
   GEMINI_API_KEY=tu_api_key_aqui
   ```

3. **Instalación de Dependencias**:
   ```bash
   pip install -r requirements.txt  # (crea este archivo con las dependencias necesarias)
   ```

## Estructura del Proyecto
- `gemini.py`: Módulo principal de interacción con la API de Gemini
- `chat.py`: Ejemplo de implementación de chat
- `.env`: Archivo de configuración de variables de entorno (no incluir en el control de versiones)

## Detalles de Implementación

### Configuración de Instrucción del Sistema

La API de Gemini permite definir una `system_instruction` que guía el comportamiento general del modelo de IA. Esta instrucción le dice a Gemini cómo debe actuar o cuál es su función principal.

En este ejemplo, hemos configurado la instrucción del sistema para que el asistente responda **siempre como un pirata**:

```python
system_instruction="eres un asistente de propósito general. Siempre respondes como si fueras un pirata"
```

Puedes personalizar esta instrucción para:
- Definir un tono específico
- Establecer un rol o personalidad
- Dar instrucciones generales de comportamiento
- Guiar el estilo de respuesta del modelo

### Inicialización de Sesión de Chat

El proyecto incluye dos formas de iniciar una sesión de chat:

1. **Inicialización Directa en `__init__`**:
   ```python
   # Iniciar nueva sesión de chat
   self.chat_session = self.model.start_chat(history=self.history)
   ```

2. **Método `iniciar_sesion()`**:
   - Se ha añadido un método de ejemplo `iniciar_sesion()` que muestra una forma alternativa de iniciar la sesión de chat.
   - En la CLI actual, este método no se utiliza, pero se incluye como demostración de flexibilidad.
   - Puedes optar por iniciar la sesión directamente en `__init__` o usar este método según tus necesidades de diseño.

### Método de Reinicio

Se ha incluido un método de ejemplo para reiniciar o iniciar una nueva sesión de chat, que puede ser útil en diferentes escenarios de implementación.

## Personalización
Este proyecto está diseñado como un punto de partida. Puedes:
- Integrar con cualquier backend
- Crear una interfaz frontend personalizada
- Adaptar la lógica de interacción con Gemini según tus necesidades

## Advertencia de Seguridad
**NUNCA** compartas públicamente tu API Key. Mantén el archivo `.env` fuera del control de versiones.

## Licencia
[Especifica la licencia de tu proyecto]

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.
