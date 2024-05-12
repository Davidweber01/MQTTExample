import paho.mqtt.client as mqtt

# MQTT broker address and port
broker_address = "ea-pc165.ei.htwg-konstanz.de"
broker_port = 1883

# MQTT topics
sensor_topic = "/SysArch/Sensor"
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

# Function to handle incoming sensor data
def on_message(client, userdata, message):
    temperature = int(message.payload.decode())
    print(f"Received temperature: {temperature}")
    # Check if the temperature is in the specific range
    if 25 <= temperature <= 28:
        print("Temperature in the desired range. Sending message to the Actor.")
        client.publish(actor_topic, "Temperature in desired range")

client.on_message = on_message

# Subscribe to the sensor topic
client.subscribe(sensor_topic)

# Loop indefinitely to receive messages
client.loop_forever()
