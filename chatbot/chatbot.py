import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import SnowballStemmer
from keras.models import load_model

class chatBot():
    def __init__(self) -> None:
        self.stemmer = SnowballStemmer("spanish")
        self.intents = json.loads(open('./chatbot/intents.json', encoding='utf-8').read())
        self.words = pickle.load(open('./chatbot/words.pkl', 'rb'))
        self.classes = pickle.load(open('./chatbot/classes.pkl', 'rb'))
        self.model = load_model('./chatbot/chatbot_model.h5')
        self.conversacion = []

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence, language='spanish')
        sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]  
        return sentence_words

    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        max_index = np.argmax(res)
        category = self.classes[max_index]
        return category

    def get_response(self, tag, intents_json):
        list_of_intents = intents_json['intents']
        result = ""
        for i in list_of_intents:
            if i["tag"] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def llenarJson(self, message):
        ints = self.predict_class(message)
        res = self.get_response(ints, self.intents)
        self.conversacion.append({"Cliente": message, "TommyFood": res})

    def guardarJson(self):
        with open("./chatbot/conversacion.json", "w") as archivo_json:
            json.dump(self.conversacion, archivo_json, indent=4)
        print("Conversación guardada en 'conversacion.json'.")
