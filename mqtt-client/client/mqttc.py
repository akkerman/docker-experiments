import signal
import paho.mqtt.client as mqtt

client = mqtt.Client()

def disconnect(signum, frame):
    client.publish('status/mqttc', 'offline', qos=0, retain=True)
    client.loop()
    client.disconnect()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish('status/mqttc', 'online', qos=0, retain=True)
    client.subscribe([('development/#', 1), ('research/#', 1)])

def on_disconnect(client, userdat, rc):
    if rc == 0:
        print("disconnected")
        sys.exit(0)
    print("unexpected disconnect")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_message_development(client, userdata, msg):
    print("processing development")

def on_message_research(client, userdata, msg):
    print("processing research")


def setup():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.will_set('status/mqttc', payload="disconnected", qos=1, retain=True)
    client.message_callback_add("development/#", on_message_development)
    client.message_callback_add("research/#", on_message_research)
    print('connecting')
    client.connect('broker', 1883, 60)
    signal.signal(signal.SIGINT, disconnect)
    signal.signal(signal.SIGTERM, disconnect)


setup()
client.loop_forever()
