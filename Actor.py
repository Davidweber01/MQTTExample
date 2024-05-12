import paho.mqtt.client as mqtt

# MQTT broker address and port
broker_address = "ea-pc165.ei.htwg-konstanz.de"
broker_port = 1883

# MQTT topic to publish to
actor_topic = "/SysArch/Actor"

# Message to send
message = "Hello, MQTT!, from Python"

# MQTT username and password
mqtt_username = ""
mqtt_password = ""
# MQTT client setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set username and password
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Connect to the MQTT broker
client.connect(broker_address)

# Function to handle incoming messages
def on_message(client, userdata, message):
    action = message.payload.decode()
    print(f"Received action: {action}")
    # Perform the desired action (printing in this example)
    print("Actor performing action:", action)

client.on_message = on_message

# Subscribe to the actor topic
client.subscribe(actor_topic)

# Loop indefinitely to receive messages
client.loop_forever()
