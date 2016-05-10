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
        msg = state_update.event_notification.event.chat_message.message_content.segment[0].text
        print("Message captured: ",msg)
        if(state_update.event_notification.event.self_event_state.user_id.chat_id != state_update.event_notification.event.sender_id.chat_id):
            processMsg(msg, CONVERSATION_ID)

def processMsg(msg, cid):
    os.system("python send_message.py \""+ cb.ask(msg.replace("@bot","")) +"\" "+cid)


if __name__ == '__main__':
    main()
