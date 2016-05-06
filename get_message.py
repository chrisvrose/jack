#!python3
import asyncio
import hangups
import sys
from google.protobuf import descriptor_pb2

REFRESH_TOKEN_PATH = 'refresh_token.txt'
CONVERSATION_ID = 'DEFAULT: UgzTQ7JmCpWG_Peinjx4AaABAagB_IuSBQ'
MESSAGE = 'Test Message'

def main():
    cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    client.on_state_update.add_observer(on_state_update)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())

@asyncio.coroutine
def on_state_update(state_update):
    
    if state_update.HasField('conversation'):
        print(state_update.conversation)
        CONVERSATION_ID = state_update.conversation.conversation_id.id
        msg = state_update.event_notification.event.chat_message.message_content.segment[0].text
        print("ConversationId: ",CONVERSATION_ID)
        print("msg: ",msg)
    
    # request = hangups.hangouts_pb2.SendChatMessageRequest(
    #     request_header=client.get_request_header(),
    #     event_request_header=hangups.hangouts_pb2.EventRequestHeader(
    #         conversation_id=hangups.hangouts_pb2.ConversationId(
    #             id=CONVERSATION_ID
    #         ),
    #         client_generated_id=client.get_client_generated_id(),
    #     ),
    #     message_content=hangups.hangouts_pb2.MessageContent(
    #         segment=[hangups.ChatMessageSegment(MESSAGE).serialize()],
    #     ),
    # )

    # try:
    #     # Make the request to the Hangouts API.
    #     yield from client.send_chat_message(request)
    # finally:
    #     # Disconnect the hangups Client to make client.connect return.
    #     yield from client.disconnect()


if __name__ == '__main__':
    main()
