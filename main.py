import paho.mqtt.client as mqttClient
import time
import json
import ast
import os
import sys

def find_data_file(filename):
    "Finds files for use in a built exe"
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "dguasmzerbcihTRIDSCVAvypkxqntfwlojJFMZGKHYXUENOWLBQP" #decription

data = open(find_data_file("data.txt"), "r")
data = ast.literal_eval(data.read())

password = ''
for i in data['pass']:
    if i in key:
        x = key.index(i)
        password += alph[x]
    else:
        password += i

data['pass'] = password

for key in data:
    print(key, data[key])

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(payload, type(payload))
    
    if payload == "report":
        print("sending data")
        out = {'Status': "on"}
        jsonOut = json.dumps(out)
        client.publish(data['publish'],jsonOut)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")

Connected = False 

current_milli_time = lambda: int(round(time.time() * 1000))

clientId = data["name"] + "-status:" + str(current_milli_time())

client = mqttClient.Client(clientId)
client.username_pw_set(data["user"], password=data["pass"])
client.on_message= on_message
client.on_connect = on_connect
client.connect(data["address"], port=data["port"])
client.loop_start()
 
while Connected != True:
    time.sleep(0.1)
    print("not connected")

client.subscribe(data["listen"])

while True:
    time.sleep(1)
