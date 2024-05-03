from paho.mqtt import client as mqtt_client
from ...models import SensorData
from random import randint
from json import loads
from django.core.management.base import BaseCommand

broker = '192.168.77.104'
port = 1883
topic = 'sensor/data'
client_id = f'subscribe-{randint(0, 100)}'

class Command(BaseCommand):
    help = 'Starts the MQTT subscriber'

    def handle(self, *args, **kwargs):
        def connect_mqtt() -> mqtt_client:
            def on_connect(client, userdata, flags, rc):
                if rc == 0:
                    print("Connected to MQTT Broker!")
                else:
                    print("Failed to connect, return code %d\n", rc)

            client = mqtt_client.Client(client_id)
            client.username_pw_set('test-subscribe', '12345aass')
            client.on_connect = on_connect
            client.connect(broker, port)
            return client

        def subscribe(client: mqtt_client):
            def on_message(client, userdata, msg):
                data = loads(msg.payload.decode())
                SensorData.objects.create(
                    rain = data['rain'],
                    light = data['light'],
                    humidity = data['humidity'],
                    temperature = data['temperature']
                )

                print(f"Data saved: {data}")

            client.subscribe(topic)
            client.on_message = on_message

        client = connect_mqtt()
        subscribe(client)
        client.loop_forever()


