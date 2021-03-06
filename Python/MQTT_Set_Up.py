from config import *
import paho.mqtt.client as mqtt

mqtt_server_host = "192.168.4.136"
mqtt_server_port = 1883
mqtt_keepalive = 60

def on_connect(client, userdata, flags, rc):
	print("Result from connect: {}".format(mqtt.connack_string(rc)))
	client.subscribe("pick-by-laser/test", qos = 0)

def on_subscribe(client, userdata, mid, granted_qos):
	print("I've subscribed with QoS: {}".format(granted_qos[0]))

def on_message(client, userdata, msg):
	print("Message received. Topic: {}. Payload: {}".format(msg.topic,str(msg.payload)))

<<<<<<< HEAD

#comment

=======
>>>>>>> 8caeb2f971d76f0fba8d9601b41eb5a016be4043
if __name__ == "__main__":
	client = mqtt.Client(protocol=mqtt.MQTTv311)
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message

	client.connect(host=mqtt_server_host, port=mqtt_server_port, keepalive=mqtt_keepalive)
	client.loop_forever()
