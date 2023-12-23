from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  
from chatbot.chatbot import chatBot

app = Flask(__name__)
CORS(app)  
chatbot = chatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    #mensaje = request.form['mensaje']
    mensaje = request.json.get('mensaje', '')
    intent = chatbot.predict_class(mensaje)
    respuesta = chatbot.get_response(intent, chatbot.intents)
    chatbot.llenarJson(mensaje)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

