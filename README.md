# MQTT-Communication
publisher.py file publishes the temp and humidity values to the topic.
subscriber.py subscribes the topic and displays the values.
values are uploaded after 1 min
This project also store the values in mongodb database
MQTT broker mosquitto is used in this project
An alert mail is sent by the subscriber if the average of humidity is greater than 80 for more than 5 minutes.
