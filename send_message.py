#!python3
import asyncio
import hangups
from sys import argv

## Some conversation IDs for testing.
# Rithvik Vibhu: UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ
# ToSE group:  UgyT6DYhh50bUOijMVh4AaABAQ
# ToSE DevTest group: Ugx56o6iNATAA80XrKp4AaABAQ
# Test group: Ugw-YMKhMfDDCpS7KiV4AaABAQ

# Path where OAuth refresh token is saved, allowing hangups to remember yourcredentials.
REFRESH_TOKEN_PATH = 'refresh_token.txt'

def sendHangoutsMessage(msg, cid=None):
    
    if cid == None:
        cid = 'UgyT6DYhh50bUOijMVh4AaABAQ'
    cid = cid.replace("Dev","Ugx56o6iNATAA80XrKp4AaABAQ")
    cid = cid.replace("ToSE","UgyT6DYhh50bUOijMVh4AaABAQ")
    cid = cid.replace("Rithvik","UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ")
    
    print("Sending hangouts message: ", msg, "\nTo: ",cid)
    
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_connect.add_observer(lambda: asyncio.async(send_message(client,msg,cid)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())

@asyncio.coroutine
def send_message(client,msg,cid):
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
    finally:
        # Disconnect the hangups Client to make client.connect return.
        yield from client.disconnect()


if __name__ == '__main__':

    if len(argv)==1: MESSAGE = "Yolo"        #No arguments - Why, don't ask us, its your job to provide a message argument dude
    else: MESSAGE = argv[1]
    
    if len(argv) == 3: CONVERSATION_ID = argv[2]
    else: CONVERSATION_ID = None
    
    sendHangoutsMessage(MESSAGE, CONVERSATION_ID)
else:
    print("[send] ",__name__, " module loaded")
