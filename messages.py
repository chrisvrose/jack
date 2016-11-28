#!/usr/bin/env python3
import asyncio
import hangups
import sys, os
import random
import time
import json
#from pprint import pprint
from google.protobuf import descriptor_pb2


import cbot
import et

REFRESH_TOKEN_PATH = 'refresh_token.txt'    # Stores the refresh token after using a auth token once
nresp = True


# Opens the database for checking up reponses
with open('prop.json') as data_file:
   data = json.load(data_file)
   print("Successfully imported Settings")
with open('feeds.json') as data_file:
   feeds = json.load(data_file)
   print("Successfully imported Feeds")

print("Opened")
print("Name:",data["name"])

def main():
    global client
    nresp = True
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
        # Join all message segments into one piece properly, and not have one message segment
        msg = " ".join([state_update.event_notification.event.chat_message.message_content.segment[x].text for x in segment_length])
        pmsg = msg.lower()
        if(state_update.event_notification.event.self_event_state.user_id.chat_id != state_update.event_notification.event.sender_id.chat_id):
            print("Message captured: ",msg)
            if pmsg.startswith((data["name"].lower()+",")):
                tmsg = pmsg[(len(data['name'])+1):].strip()
                if "exit" in pmsg:
                    sys.exit(0)
                elif tmsg in data["question"]:
                    resp = format_and_replace(random.choice(data["question"][tmsg]),CONVERSATION_ID)
                    processMsg(resp,CONVERSATION_ID)
                elif "sleep" in tmsg:
                    snresp(False);
                elif "wake" in tmsg:
                    snresp(True);
                elif "give me " in tmsg or "get me" in tmsg:
                    query = tmsg.replace("give me ","")
                    ep = query.split(" of ")[0].strip();
                    show = query.replace(ep+" of ","").strip();
                    url = processQuery(show,ep)
                    processMsg(url,CONVERSATION_ID)
                else:
                    processMsg(random.choice(data["invalid"]),CONVERSATION_ID)
            else:
                if(qnresp()==True):
                    processMsg(msg, CONVERSATION_ID, 1)
                    print(qnresp())
                else:
                    print("Sleeping. Ignoring.")

def snresp(bv):
    global nresp
    nresp = bv
    print("New state,",nresp)

def qnresp():
    return nresp


# To substitute some things into answers
def format_and_replace(msg,cid="Unavailable"):
    if "(Name)" in msg:
        msg = msg.replace("(Name)", data["name"])
    if "(Time)" in msg:
        msg = msg.replace("(Time)", time.strftime('%l:%M%p, %b %d %Y'))
    if "(Time+z)" in msg:
        msg = msg.replace("(Time+z)",  time.strftime('%l:%M%p, %b %d %Y, %z'))
    if "(cid)" in msg:
        msg = msg.replace("(cid)", cid)
    if "(list)" in msg:
        msg = msg.replace("(list)", json.dumps(data["question"]))
    if "(status)" in msg:
        msg = msg.replace("(status)",("awake" if qnresp() else "sleeping"))
    return msg

def processQuery(show,ep):
    for a,b in feeds.items():
        print(show," ",a," ",b["on"])
        if show in b["on"]:
            return(et.search(a,ep))


def processMsg(msg, cid,rep = 0):
    # This is implemented like such - passing true to the function uses the cleverbot function, else the message is sent as such
    if(rep==1):
        #reply = cb.ask(msg)
        reply = cbot.ask(msg)
        print("[processMsg]", reply)
        asyncio.async(send_message(client,reply,cid))
    else:
        asyncio.async(send_message(client,msg,cid))



def send_message(client,msg,cid):
    print("[send_message] - ",msg)
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
else:
    print("[get_message]:loaded")
