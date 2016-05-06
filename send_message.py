#!python3
import asyncio
import hangups
from sys import argv

# ID of the conversation to send the message to.
# CONVERSATION_ID = 'UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ'
#Handling the message





if len(argv)==1: 
    MESSAGE = "Yolo"        #No arguments - Why, don't ask us
else: 
    MESSAGE = argv[1]
    
#Handling the Conversation ID
if len(argv) == 3:
    CONVERSATION_ID = argv[2]        #Set input Conversation id
else:
    CONVERSATION_ID = 'UgyT6DYhh50bUOijMVh4AaABAQ'        #Post to the Tose Group

CONVERSATION_ID= CONVERSATION_ID.replace("Dev","UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ");
CONVERSATION_ID= CONVERSATION_ID.replace("ToSE","UgyT6DYhh50bUOijMVh4AaABAQ");


## Some conversation IDs for testing.
# Rithvik Vibhu: UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ
# ToSE group:  UgyT6DYhh50bUOijMVh4AaABAQ
# ToSE DevTest group: Ugx56o6iNATAA80XrKp4AaABAQ
# Test group: Ugw-YMKhMfDDCpS7KiV4AaABAQ

# print(MESSAGE, CONVERSATION_ID)

#Below code removed as this confirmation is not really required as the header is returned
#print("Sent hangouts message: ", MESSAGE)

# Path where OAuth refresh token is saved, allowing hangups to remember yourcredentials.
REFRESH_TOKEN_PATH = 'refresh_token.txt'

## Default stuff ahead.

def main():
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_connect.add_observer(lambda: asyncio.async(send_message(client)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())

@asyncio.coroutine
def send_message(client):

    request = hangups.hangouts_pb2.SendChatMessageRequest(
        request_header=client.get_request_header(),
        event_request_header=hangups.hangouts_pb2.EventRequestHeader(
            conversation_id=hangups.hangouts_pb2.ConversationId(
                id=CONVERSATION_ID
            ),
            client_generated_id=client.get_client_generated_id(),
        ),
        message_content=hangups.hangouts_pb2.MessageContent(
            segment=[hangups.ChatMessageSegment(MESSAGE).serialize()],
        ),
    )

    try:
        # Make the request to the Hangouts API.
        yield from client.send_chat_message(request)
    finally:
        # Disconnect the hangups Client to make client.connect return.
        yield from client.disconnect()


if __name__ == '__main__':
    main()
