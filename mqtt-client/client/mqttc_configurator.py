""" generic way to create a mqtt client
    with it's own event loop and doesn't block
    to be able to respond to shutdown signals """

import sys
import signal
import threading
import paho.mqtt.client as mqtt

def mqttc_configurator(name=None, subscribe_to=None, loop_delay=60.0):
    """ configure mqttc and a shutdown handler """
    assert name is not None
    assert loop_delay > 1

    lwt_topic = 'status/' + name
    client = mqtt.Client()

    def on_connect(client, userdata, flags, resultcode):
        """ handle connection established to mqtt broker """
        print('Connected with result code', resultcode, 'and flags', flags)
        print('got userdata: ', userdata)

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.publish(lwt_topic, 'online', qos=0, retain=True)
        if subscribe_to is not None:
            client.subscribe(subscribe_to)

    def on_disconnect(client, userdata, resultcode): # pylint: disable=W0613
        """ handle disconnect from mqtt broker """
        if resultcode == 0:
            print("disconnected")
            sys.exit(0)
        print("unexpected disconnect")

    def add_signal_handler():
        """ add a signal handler to SIGINT and SIGTERM """
        def signal_handler(signum, frame):
            """ handle system signals, disconnect mqtt """
            print('recieved signal', signum, frame)
            client.publish(lwt_topic, 'offline', qos=0, retain=True)
            client.loop()
            client.disconnect()
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

    def configure_client():
        """ configure the mqtt client """
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.will_set('status/mqttc', payload="disconnected", qos=1, retain=True)
        print('connecting')
        client.connect('broker', 1883, 60)

    def start_loop(func):
        """ start looping the given function """
        def looper():
            """ schedule itself every 'loop_delay' seconds """
            threading.Timer(loop_delay, looper).start() # called every minute
            func()
        looper()

    configure_client()
    add_signal_handler()
    loop = yield client
    start_loop(loop)
    client.loop_forever()
    yield
