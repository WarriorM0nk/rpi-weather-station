from gpiozero import MCP3008

import board
import adafruit_dht

def rain(channel_number):
    return MCP3008(channel = channel_number)

def light(channel_number):
    return MCP3008(channel = channel_number)

def humidity_temperature():
    return adafruit_dht.DHT11(board.D22, use_pulseio = False)
