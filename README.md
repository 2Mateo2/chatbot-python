Este proyecto que he desarrollado es un chatbot implementado en Python utilizando Flask para crear un servidor web. También he utilizado las bibliotecas NLTK y Keras para el procesamiento de lenguaje natural y la creación de un modelo de aprendizaje profundo.

Voy a describir cada uno de los archivos del proyecto:

app.py:

Aplicación Flask: Inicia una aplicación web Flask.
Rutas:
/: Devuelve una página HTML, posiblemente un formulario de chat.
/chat (POST): Recibe mensajes del usuario, utiliza el chatbot para procesarlos y devuelve la respuesta.
training.py:

Entrenamiento del Modelo:
Carga datos de entrenamiento desde intents.json.
Utiliza NLTK para tokenizar y procesar el texto.
Entrena un modelo de red neuronal utilizando Keras con SGD como optimizador.
Guarda el modelo entrenado y otros datos relevantes para su uso posterior por el chatbot.
chatbot.py:

Clase ChatBot:
Carga el modelo de la red neuronal entrenado y otros datos esenciales (palabras, clases, intenciones) desde archivos pickle y JSON.
Tokeniza y procesa el texto del usuario utilizando NLTK.
Utiliza el modelo de red neuronal para predecir la clase de la intención del usuario.
Retorna respuestas generadas aleatoriamente basadas en las intenciones.
Funcionamiento:

El usuario envía mensajes al chatbot a través de la interfaz web.
El chatbot procesa los mensajes, predice la intención y genera respuestas.

Requerimientos:

pip install Flask flask-cors nltk tensorflow 

Intrucciones para ejecutar el chatbot con exito:

1. Primero debe irse al arhivo trainning.py y correr el archivo
Aqui se generara el entramiento del chatbot

2. Correr la app desde el archivo app.py
Aqui es donde se inicializa la aplicacion

3. Probarla desde un Herramientas de Desarrollo de API ya sea esta postman o insonia, incluso la puedes probar desde un formulario html
Esta es la ruta: http://localhost:5000/chat
