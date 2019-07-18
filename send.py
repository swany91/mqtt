import paho.mqtt.client as mqtt
from colorama import Fore, Style

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("gc/trio")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.1.5", 1883, 60)


while True:
	message = input('Your message: ')
	new_message = Fore.RED + Style.BRIGHT + message
	client.publish('gc/trio ' , new_message)


