#!python3
import asyncio
import hangups
import sys, os
import random
from google.protobuf import descriptor_pb2
from cleverbot import Cleverbot


cb = Cleverbot()


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
        print(state_update.event_notification.event.chat_message.message_content.segment);
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
        namer = name.read().rstrip()  #Read file and strip trailing spaces and newlines also
    name.close()
 
    if namer.lower() in msg.lower():
        os.system("python send_message.py \""+ cb.ask(msg) +"\" "+cid)


if __name__ == '__main__':
    main()


