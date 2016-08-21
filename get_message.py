#!python3
import asyncio
import hangups
import sys, os
import random
import time
import json
#from pprint import pprint
from google.protobuf import descriptor_pb2
from cleverbot import Cleverbot

# Calls up the cleverbot instance
cb = Cleverbot()


REFRESH_TOKEN_PATH = 'refresh_token.txt'    # Stores the refresh token after using a auth token once

with open('prop.json') as data_file:
   data = json.load(data_file)

#print(data)
#print(data["name"])

def main():
    global client
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_state_update.add_observer(on_state_update)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())

@asyncio.coroutine
def on_state_update(state_update):
    if (state_update.HasField('conversation')):
        #if (state_update.HasField('conversation') and (state_update.conversation.type != 'CONVERSATION_TYPE_ONE_TO_ONE')):
        #print(state_update.conversation)
        CONVERSATION_ID = state_update.conversation.conversation_id.id
        segment_length = range(len(state_update.event_notification.event.chat_message.message_content.segment))
        #msg = state_update.event_notification.event.chat_message.message_content.segment[0].text
        # Join all message segments into one piece properly, and not have one message segment
        msg = " ".join([state_update.event_notification.event.chat_message.message_content.segment[x].text for x in segment_length])
        pmsg = msg.lower()
        if(state_update.event_notification.event.self_event_state.user_id.chat_id != state_update.event_notification.event.sender_id.chat_id):
            print("Message captured: ",msg)
            #print(state_update.event_notification.event.chat_message)
            if pmsg.startswith((data["name"].lower()+",")):
                tmsg = pmsg[(len(data['name'])+1):].strip()
                print(tmsg)
                if "identify" in pmsg:
                    processMsg(("Its me, "+data["name"]+"!"),CONVERSATION_ID)
                if "exit" in pmsg:
                    sys.exit(0)
                if "cid" in pmsg:
                    processMsg(CONVERSATION_ID,CONVERSATION_ID)
                if "time" in pmsg:
                    stime = time.strftime('%l:%M%p, %b %d %Y, %z')
                    processMsg(stime,CONVERSATION_ID)
                if tmsg in data:
                    processMsg(random.choice(data[tmsg]),CONVERSATION_ID)
            else:
                processMsg(msg, CONVERSATION_ID, 1)



def processMsg(msg, cid,rep = 0):
    # This is implemented like such - passing true to the function uses the cleverbot function, else the message is sent as such
    if(rep==1):
        reply = cb.ask(msg)
        print("[processMsg]", reply)
        asyncio.async(send_message(client,reply,cid))
    else:
        asyncio.async(send_message(client,msg,cid))




def send_message(client,msg,cid):
    print("[send_message]")
    request = hangups.hangouts_pb2.SendChatMessageRequest(
        request_header=client.get_request_header(),
        event_request_header=hangups.hangouts_pb2.EventRequestHeader(
            conversation_id=hangups.hangouts_pb2.ConversationId(
                id=cid
            ),
            client_generated_id=client.get_client_generated_id(),
        ),
        message_content=hangups.hangouts_pb2.MessageContent(
            segment=[hangups.ChatMessageSegment(msg).serialize()],
        ),
    )

    try:
        # Make the request to the Hangouts API.
        yield from client.send_chat_message(request)
    except:
        print("ERROR::",sys.exc_info()[0])



if __name__ == '__main__':
    main()
