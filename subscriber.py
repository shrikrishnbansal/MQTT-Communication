import paho.mqtt.client as paho
import time
import sys
import datetime
import time
import smtplib

sender = 'shrikrishnbansal@gmail.com'
receivers = ['piyushbansal@gmail.com']
broker="localhost"  #host name
topic="test" #topic name
humArray = []
humAverage = 0
        
def on_message(client, userdata, message):
  print("received data is :")  
  print(str(message.payload.decode("utf-8")) ) #printing Received message
  print("")
  m_decode=str(msg.payload.decode("utf-8","ignore"))
  m_in=json.loads(m_decode) #decode json data
  hum_value = m_in["Humidity"]
  if(len(humArray)==6):
    humArray.pop(0)
    humArray.append(hum_value)
    humAverage = sum(humArray)/len(humArray)
  else:
    humArray.append(hum_value)

  if(humAverage>80):
    message = """From: From Person <shrikrishnbansal@gmail.com>
    To: To Person <piyushbansal@gmail.com>
    Subject: Humidity Warning

    This is a warning raised for humidity values as it is greater than 80.
    """
    try:
     smtpObj = smtplib.SMTP('localhost')
     smtpObj.sendmail(sender, receivers, message)         
     print "Successfully sent email"
    except SMTPException:
     print "Error: unable to send email"
    
client= paho.Client("user") #create client object 
client.on_message=on_message
   
print("connecting to broker host",broker)
client.connect(broker)#connection establishment with broker
print("subscribing begins here")    
client.subscribe(topic)#subscribe topic test

while 1:
    client.loop_start() #contineously checking for message 
