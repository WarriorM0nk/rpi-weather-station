from json import dumps
from paho.mqtt import client as mqtt_client
from time import sleep 
from random import randint

from Sensor.sensor import rain, light, humidity_temperature
from Sensor.normalize import normalize

broker = '192.168.77.104'
port = 1883
topic = 'sensor/data'
client_id = f'publish-{randint(0, 1000)}'

def connect_mqtt():
    def on_connect():
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print('Failed to connect, return code {rc}\n')

    client = mqtt_client.Client(client_id)
    client.username_pw_set('test-publish', '12345aass')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def get_sensor_data():
    rainValue = normalize(rain(7).value)
    lightValue = normalize(light(6).value)
    humidityValue = humidity_temperature().humidity
    temperatureValue = humidity_temperature().temperature

    values = {
        "rain":rainValue, 
        "light":lightValue,
        "humidity":humidityValue,
        "temperature":temperatureValue,
    }

    return dumps(values)

def publish(client):
    msg_count = 1
    while True:
        data = get_sensor_data()

        msg = str(data)
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print("sent")
        else:
            print(f"Failed to send message to topic {topic}")
        
        msg_count += 1
        if msg_count > 5:
            break

        sleep(1)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

if __name__ == "__main__":
    run()
