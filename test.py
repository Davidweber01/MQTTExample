import paho.mqtt.client as mqtt

# MQTT broker address and port
broker_address = "ea-pc165.ei.htwg-konstanz.de"
broker_port = 1883

# MQTT topic to publish to
topic = "/SysArch/test"

# Message to send
message = "Hello, MQTT!, from Python"

# MQTT username and password
mqtt_username = ""
mqtt_password = ""

# Callback function for when a connection is established to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.publish(topic, message)
        print("Message published successfully")
    else:
        print("Failed to connect to MQTT broker")

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set username and password
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Assign callback functions
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT client loop to handle network communication and callbacks
client.loop_forever()
