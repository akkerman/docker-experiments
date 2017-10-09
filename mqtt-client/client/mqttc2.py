""" specific mqtt client """
from mqttc_configurator import  mqttc_configurator


TOPIC_DEVELOPMENT = 'development/#'
TOPIC_RESEARCH = 'research/#'

def on_message_development(client, userdata, msg):
    """ handle message on topic develop """
    print("processing development")

def on_message_research(client, userdata, msg):
    """ handle message on topic research """
    print("processing research")

def loop():
    """ perform the loop """
    print('loop')

def setup():
    """ configure this mqtt client """
    config = mqttc_configurator(
        client_id='mqttc2',
        subscribe_to=[(TOPIC_DEVELOPMENT, 1), (TOPIC_RESEARCH, 2)],
        loop_delay=60.0
        )

    client = next(config)
    client.message_callback_add(TOPIC_DEVELOPMENT, on_message_development)
    client.message_callback_add(TOPIC_RESEARCH, on_message_research)
    config.send(loop)
    # config.send(None)

setup()
