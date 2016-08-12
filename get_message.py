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
    global client
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
            if msg.lower().startswith("@bot"):
                if "identify" in msg.lower():
                    send_message("Its me, Jack!",CONVERSATION_ID)
                if "stfu" in msg.lower():
                    send_message("Shutting Down",CONVERSATION_ID)
                    sys.exit(0)
                if "cid" in msg.lower():
                    send_message(CONVERSATION_ID,CONVERSATION_ID)
            else:
                processMsg(msg, CONVERSATION_ID)

def processMsg(msg, cid):
    reply = cb.ask(msg)
    print("[get][processMsg]", reply)
    asyncio.async(send_message(client,reply,cid))


def send_message(client,msg,cid):
    print("[get] Running send_message")
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
