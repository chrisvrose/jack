#!/usr/bin/env python3
#from chatterbot import ChatBot
from cleverbot import Cleverbot
cb = Cleverbot()
#chatbot = ChatBot(
#	'Jack Carlson',
#	storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
#	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
#	logic_adapters=[
#		"chatterbot.adapters.logic.MathematicalEvaluation",
#		"chatterbot.adapters.logic.TimeLogicAdapter"
#	],
#	database="./database.json"
#)
#chatbot.train("chatterbot.corpus.english")

def ask(query):
	#reply = str(chatbot.get_response(query))
	reply = cb.ask(query)
	return(reply)
