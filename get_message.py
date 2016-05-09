#!python3
import asyncio
import hangups
import sys, os
import random
from google.protobuf import descriptor_pb2

REFRESH_TOKEN_PATH = 'refresh_token.txt'    #Stores the refresh token after using a auth token once

def main():
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_state_update.add_observer(on_state_update)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())

@asyncio.coroutine
def on_state_update(state_update):
    
    if state_update.HasField('conversation'):
        # print(state_update.conversation)
        CONVERSATION_ID = state_update.conversation.conversation_id.id
        msg = state_update.event_notification.event.chat_message.message_content.segment[0].text
        #print("ConversationId: ",CONVERSATION_ID)
        print("Message captured: ",msg)
        processMsg(msg, CONVERSATION_ID)



def processMsg(msg, cid):
    name = open('name.txt','a+')
    namer = ""
    name.seek(0) #ensure you're at the start of the file..
    first_char = name.read(1) #get the first character
    if not first_char:
        name.write("Tose")
    else:
        name.seek(0)  #make sure you are still at the start of the file
        namer = name.read()
    print(namer.lower())
    name.close()
    if msg.lower().startswith(namer.lower()):
        if "lol me" in msg.lower():
            randomMessages = ["I don\'t hold grudges, my father did and I always hated him for it", " Say what you want about deaf people..."," My wife and I were happy for twenty years; then we met.", "My grandfather has the heart of a lion and a lifetime ban from the local zoo.","When you throw a boomerang and it doesnt return, you lost a stick","I refused to believe my roadworker father was stealing from his job, but when I got home, all the signs were there.","I haven\'t slept for three days, because that would be too long","There\'s a fine line between Numerator and Denominator."]
            os.system("python send_message.py \""+ random.choice(randomMessages) +"\" "+cid)
        elif "what do you think about dc comics" in msg.lower() or "what do you think of dc comics" in msg.lower():
            randomMessages = ["Greg! Move your Head!","Its quite a Marvel.","It sure is quite a marvel."]
            os.system("python send_message.py \""+ random.choice(randomMessages) +"\" "+cid)
        elif "i am spartacus" in msg.lower():
            randomMessages = ["But I am Spartacus!","No! I am Spartacus!", "How dare you! I am Spartacus"]
            os.system("python send_message.py \""+random.choice(randomMessages)+"\" "+cid)
        elif "yolo" in msg.lower():
            randomMessages = ["Yolo - Always remember to wear your seat belt!","Yolo - Never jump off a cliff riding a pig!","Yolo - You never live twice!","Yolo - Gringott. Try saying that. Gring-gott. Teehee", "Yolo - 12345 is a bad password!", "Yolo : Any computer is a laptop if you're brave enough!"]
            os.system("python send_message.py \""+random.choice(randomMessages)+"\" "+cid)
        elif "gimme the cid" in msg.lower():
            os.system("python send_message.py \""+cid+"\" "+cid)
        elif "how was batman vs superman" in msg.lower():
            randomMessages = ["The red capes are coming! The red capes are coming!","Devils don\'t come from beneath us, they come from the skies.","Do you bleed? You probably will but I\'m a bot so I can\'t really harm you"]
            os.system("python send_message.py \""+random.choice(randomMessages)+"\" "+cid)
        else:
            randomMessages = ["Get mad!","Don\'t make lemonade","Goodbye.","Her name is Caroline","The answer is beneath us","Hello...","Prometheus was punished by the gods for giving the gift of knowledge to man. He was cast into the bowels of the Earth and pecked by birds.","sqrt(-1) love you!"]
            os.system("python send_message.py \""+random.choice(randomMessages)+"\" "+cid)

if __name__ == '__main__':
    main()


