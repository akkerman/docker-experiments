# pylint: disable=C0111

import threading

def create_looper(func):
    def looper():
        threading.Timer(4.0, looper).start() # called every minute
        func()
    return looper

class Client(object):
    def __init__(self, name, subscribe_to):
        self.name = name
        self.subscribe_to = subscribe_to
    def message_callback_add(self, topic, handler):
        print(self.name, 'attach handler to ', topic, handler.__name__)
        print('current topics: ', self.subscribe_to)
    def publish(self, topic, message):
        print(self.name, 'publish', topic, message)

def client_configurator(name, subscribe_to):
    stub = Client(name, subscribe_to)
    loop = yield stub
    loop = create_looper(loop)
    loop()
    print('config done')
    yield()

#--------------------------------------------------

def on_message_research():
    pass

def on_message_development():
    pass

def create_loop(client):
    def loop():
        client.publish('test/iot', 'loop')
    return loop

def main():
    config = client_configurator(
        name='runner',
        subscribe_to=[('development/#', 1), ('research/#', 1)])

    client = next(config)

    # optional stuff
    client.message_callback_add("development/#", on_message_development)
    client.message_callback_add("research/#", on_message_research)
    # /optional stuff

    config.send(create_loop(client))

main()
