#!/usr/bin/env python3
import asyncio
import hangups
import sys, os
import random
import time
import json
from google.protobuf import descriptor_pb2
from hangups.hangouts_pb2 import (
TYPING_TYPE_STARTED, TYPING_TYPE_PAUSED, TYPING_TYPE_STOPPED,
MEMBERSHIP_CHANGE_TYPE_LEAVE, MEMBERSHIP_CHANGE_TYPE_JOIN,
HANGOUT_EVENT_TYPE_START, HANGOUT_EVENT_TYPE_END, HANGOUT_EVENT_TYPE_JOIN,
HANGOUT_EVENT_TYPE_LEAVE, HANGOUT_EVENT_TYPE_COMING_SOON,
HANGOUT_EVENT_TYPE_ONGOING, GROUP_LINK_SHARING_STATUS_OFF,
GROUP_LINK_SHARING_STATUS_ON, NOTIFICATION_LEVEL_QUIET,
NOTIFICATION_LEVEL_RING, SEGMENT_TYPE_TEXT, SEGMENT_TYPE_LINE_BREAK,
SEGMENT_TYPE_LINK, OFF_THE_RECORD_STATUS_ON_THE_RECORD,
OFF_THE_RECORD_STATUS_OFF_THE_RECORD
)
import cbot
import l33tx
import psycopg2


BROADCAST_GROUP_CID = 'UgyT6DYhh50bUOijMVh4AaABAQ'
REFRESH_TOKEN_PATH = 'refresh_token.txt'    # Stores the refresh token after using a auth token once
nresp = True
global data
global help
global llength


# Opens the database for checking up reponses
with open('prop.json') as data_file:
   data = json.load(data_file)
   llength = int(data["llength_init"])
   print("Loaded Settings")
with open('usage.txt') as data_file:
   help = data_file.read().replace('\n',' ')
   print("Loaded Usage File")
with open('feeds.json') as data_file:
   feeds = json.load(data_file)
   print("Loaded Feeds")

print("Name:",data["name"])




def parseDBURI(dburi):
    t1 = dburi.split("@")
    lhs = t1[0].split("//")[1].split(":")
    user = lhs[0]
    passw = lhs[1]
    rhs =  t1[1].split("/")
    addpport = rhs[0].split(":")
    addr = addpport[0]
    port = addpport[1]
    db = rhs[1]
    retstr = "host="+addr+" port="+port+" dbname="+db+" user="+user+" password="+passw+" sslmode=require"
    return(retstr)

if(len(sys.argv)==2):
    global conn
    conn = psycopg2.connect(parseDBURI(sys.argv[1]))
    cur = conn.cursor()
    if(!os.path.isfile('refresh_token.txt')):
        with open('refresh_token.txt) as file:
            print(cur.execute("SELECT * from reft;").fetchone())
    cur.close()
    conn.close()
    

def main():
    global client
    nresp = False
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_state_update.add_observer(on_state_update)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())
    

async def on_state_update(state_update):
    #print(state_update)
    if (state_update.HasField('typing_notification')):
        set_focus(state_update.typing_notification.conversation_id.id)
        #print("LOL")
    if (state_update.HasField('conversation')):
        #if (state_update.HasField('conversation') and (state_update.conversation.type != 'CONVERSATION_TYPE_ONE_TO_ONE')):
        #print(state_update.conversation)
        CONVERSATION_ID = state_update.conversation.conversation_id.id
        segment_length = range(len(state_update.event_notification.event.chat_message.message_content.segment))
        # Join all message segments into one piece properly, and not have one message segment
        msg = " ".join([state_update.event_notification.event.chat_message.message_content.segment[x].text for x in segment_length])
        pmsg = msg.lower()
        if(state_update.event_notification.event.self_event_state.user_id.chat_id != state_update.event_notification.event.sender_id.chat_id):
            #print("Message captured: ",msg)
            # Removing name from query
            tmsg = pmsg[(len(data['name'])+1):].replace(",","").replace(".","").strip()
            #print(str(tuple(data["question-nc"].keys()))+" "+str(tmsg.startswith(tuple(data["question-nc"].keys()))))
            # CONTEXT QUESTIONS
            if pmsg.startswith(data["name"].lower()):
                if tmsg in data["question-ci"]:
                    resp = format_and_replace(random.choice(data["question-ci"][tmsg]),CONVERSATION_ID)
                    processMsg(resp,CONVERSATION_ID)
                elif data["get-stuff-1"] in tmsg or data["get-stuff-2"] in tmsg:
                    query = tmsg.replace(data["get-stuff-1"],"").replace(data["get-stuff-2"],"")
                    ep = query.split(" of ")[0].strip();
                    show = query.replace(ep+" of ","").strip();
                    url = processQueryS(show,ep)
                    processMsg(url,CONVERSATION_ID)
                elif data["search-stuff"] in tmsg:
                    query = tmsg.replace("search ","")
                    print("Searching:",query)
                    processQueryM(query,CONVERSATION_ID)
                elif data["length"] in tmsg:
                    global llength
                    llength = int(tmsg.split(" ")[1])
                    processMsg("Length set:"+str(llength),CONVERSATION_ID)
                else:
                    if(qnresp()):
                        processMsg(msg,CONVERSATION_ID,1)
            #elif tmsg in data["question-nc"]:
            #    resp = format_and_replace(random.choice(data["question-nc"][tmsg]))
            #    processMsg(resp,CONVERSATION_ID)
            else:
                if(qnresp()):
                    processMsg(msg,CONVERSATION_ID,1)
        #asyncio.async(set_typing(CONVERSATION_ID,TYPING_TYPE_STOPPED))



def set_focus(conversation_id):
    print(conversation_id)
    request = hangups.hangouts_pb2.SetFocusRequest(
        request_header=client.get_request_header(),
        conversation_id=hangups.hangouts_pb2.ConversationId(
            id=conversation_id
        ),
        type=hangups.hangouts_pb2.FOCUS_TYPE_FOCUSED,
        timeout_secs=5,
    )
    yield from client.set_focus(request)



def set_typing(cid,typing):
    global client
    try:
        yield from client.set_typing(
            hangups.hangouts_pb2.SetTypingRequest(
                request_header=client.get_request_header(),
                conversation_id=hangups.hangouts_pb2.ConversationId(id=cid),
                type=typing,
            )
        )
    except Exception as e:
        print(e)


def snresp(bv):
    global nresp
    nresp = bv
    print("New state,",nresp)

#Return status of this variable, don't work otherwise, dunno why
def qnresp():
    return nresp


# To substitute some things into answers
def format_and_replace(msg,cid="Unavailable"):
    if "(exit)" in msg:
        sys.exit(0)
    if "(help)" in msg:
        msg = msg.replace("(help)",help)
    if "(sleep)" in msg:
        snresp(False)
        msg = msg.replace("(sleep)","")
    if "(wake)" in msg:
        snresp(True)
        msg = msg.replace("(wake)","")
    if "(Name)" in msg:
        msg = msg.replace("(Name)", data["name"])
    #if "(Time)" in msg:
    #    msg = msg.replace("(Time)", time.strftime('%l:%M%p, %b %d %Y'))
    if "(Time+z)" in msg:
        msg = msg.replace("(Time+z)",  time.strftime('%l:%M%p, %b %d %Y, %z'))
    if "(cid)" in msg:
        msg = msg.replace("(cid)", cid)
    if "(list)" in msg:
        msg = msg.replace("(list)", json.dumps(data["question"]))
    if "(llength)" in msg:
        msg = msg.replace("llength",str(llength))
    if "(status)" in msg:
        msg = msg.replace("(status)",("awake" if qnresp() else "sleeping"))
    return msg


#Processing single queries
def processQueryS(show,ep):
    b = False
    for a,b in feeds.items():
        #print(show," ",a," ",b["on"])
        if show in b["on"]:
            b = True
            return(l33tx.search(a,ep).magnet)
    if not b:
        return("Invalid selection")

#Processing multiple queries
def processQueryM(query,cid):
    global llength
    print(llength)
    replies = l33tx.search_gen(query,llength,2)
    for m,n in replies.items():
        processMsg(str(m)+" - \n"+n.title+" : \n"+n.magnet,cid)

def processMsg(msg, cid,rep = 0):
    # This is implemented like such - passing true to the function uses the cleverbot function, else the message is sent as such
    if(rep==1):
        #reply = cb.ask(msg)
        reply = cbot.ask(msg)
        print("[processMsg]", reply)
        asyncio.async(send_message(client,reply,cid))
    else:
        asyncio.async(send_message(client,msg,cid))



async def send_message(client,msg,cid):
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
        await client.send_chat_message(request)
    except:
        print("ERROR::",sys.exc_info()[0])





if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupt')
        sys.exit(0)
else:
    print("What are you trying to do? This module is usually run by main()")
    print("[get_message]:loaded")
