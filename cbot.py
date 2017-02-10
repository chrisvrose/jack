#!/usr/bin/env python3
from chatterbot import ChatBot
#from cleverbot import Cleverbot
#cb = Cleverbot()
chatbot = ChatBot(
	'Jack Carlson',
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	database="./database.json"
)
#chatbot.train("chatterbot.corpus.english")

def ask(query):
	reply = chatbot.get_response(query)
	return(str(reply))
