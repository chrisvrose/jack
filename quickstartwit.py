import sys
from wit import Wit

# Quickstart example
# See https://wit.ai/l5t/Quickstart

if len(sys.argv) != 1:
    print("usage: python examples/quickstart.py <wit-token>")
    exit(1)
access_token = 'Z7TWDMF6SI5S2MV6OPMWJR3DFLFOQYWA'

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def say(session_id, context, msg):
    print(msg)

def merge(session_id, context, entities, msg):
    loc = first_entity_value(entities, 'location')
    if loc:
        context['loc'] = loc
    return context

def error(session_id, context, e):
    print(str(e))

def fetch_weather(session_id, context):
    context['forecast'] = 'sunny [['+str(context)+']] in '+context["loc"]
    return context

def get_latest_ep(session_id, context):
    context['title'] = 'TitleGoesHere'
    context['link'] = 'LinkGoesHere'
    context['magnet'] = 'MagnetGoesHere'
    return context

def get_ep_se(session_id, context):
    context['title'] = 'SPECIFICTitleGoesHere'
    context['link'] = 'SPECIFICLinkGoesHere'
    context['magnet'] = 'SPECIFICMagnetGoesHere'
    return context

actions = {
    'say': say,
    'merge': merge,
    'error': error,
    'fetch-weather': fetch_weather,
    'get-latest-ep': get_latest_ep,
    'get-specific-ep-se': get_ep_se
}

client = Wit(access_token, actions)
client.interactive()