#!/usr/bin/env python3
from chatterbot import ChatBot
import os

global chatbot

if 'DATABASE_URL' in os.environ:
	chatbot = ChatBot(
		'Jack Carlson',
		trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	        database_uri=os.environ['DATABASE_URL']
	)
else:
	chatbot = ChatBot(
                'Jack Carlson',
                trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                database="./database.json"
        )

def ask(query):
	reply = chatbot.get_response(query)
	return(str(reply))

def clear():
	chatbot.storage.drop()
