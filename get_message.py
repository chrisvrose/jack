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
        print("ConversationId: ",CONVERSATION_ID)
        print("msg: ",msg)
        processMsg(msg, CONVERSATION_ID)



def processMsg(msg, cid):
    
    if msg.lower().startswith("tose"):
        if "lol me" in msg.lower():
            randomMessages = ["I don\'t hold grudges, my father did and I always hated him for it", " Say what you want about deaf people..."," My wife and I were happy for twenty years; then we met.", "My grandfather has the heart of a lion and a lifetime ban from the local zoo.","When you throw a boomerang and it doesnt return, you lost a stick","I refused to believe my roadworker father was stealing from his job, but when I got home, all the signs were there.","I haven\'t slept for three days, because that would be too long","There\'s a fine line between Numerator and Denominator."]
            os.system("python send_message.py \""+ random.choice(randomMessages) +"\" "+cid)
        elif "i am spartacus" in msg.lower():
            os.system("python send_message.py \"No, I am Spartacus\" "+cid)
        elif "yolo" in msg.lower():
            os.system("python send_message.py \"Yolo - Always remember to wear your seat belt!\" "+cid)
        elif "gimme the cid" in msg.lower():
            os.system("python send_message.py \"+cid+"\" "+cid)
        else:
            os.system("python send_message.py \"Yolo\" "+cid)


if __name__ == '__main__':
    main()
