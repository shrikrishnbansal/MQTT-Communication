import paho.mqtt.client as paho #mqtt library
import os
import json
import time
import random
from datetime import datetime

#host name is localhost because both broker and python are Running on same 
#machine/Computer.
broker="localhost" #host name , Replace with your IP address.
topic="test";
port=1883 #MQTT data listening port
ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j' #not manditory


def on_publish(client,userdata,result): #create function for callback
  print("published data is : ")
  pass

client1= paho.Client("control1") #create client object
client1.on_publish = on_publish #assign function to callback
client1.username_pw_set(ACCESS_TOKEN) #access token from thingsboard device
client1.connect(broker,port,keepalive=60) #establishing connection

#publishing after every 5 secs
while True:
  tempValue = random. randint(22,28)
  humidityValue = random.randint(0-100)
  payload="{"
  payload+="\"Temperature\":";payload+=tempValue;payload+=",";
  payload+="\"Humidity\":";payload+=humidityValue;
  payload+="}"
  ret= client1.publish(topic,payload) #topic name is test
  print(payload);
  print("Please check data on your Subscriber Code \n")
  time.sleep(60)
