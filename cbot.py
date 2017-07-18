#!/usr/bin/env python3
from chatterbot import ChatBot
chatbot = ChatBot(
	'Jack Carlson',
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	database="./database.db"
)

def ask(query):
	reply = chatbot.get_response(query)
	return(str(reply))
