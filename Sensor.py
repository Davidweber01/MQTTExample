import paho.mqtt.client as mqtt
import time
import random

# MQTT broker address and port
broker_address = "ea-pc165.ei.htwg-konstanz.de"
broker_port = 1883

# MQTT topic to publish to
topic = "/SysArch/Sensor"

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

# Function to simulate sensor data
def generate_sensor_data():
    while True:
        # Simulate sensor data (temperature in this example)
        temperature = random.randint(20, 30)  # Random temperature between 20 and 30
        # Publish sensor data to the topic
        client.publish(topic, str(temperature))
        time.sleep(5)  # Wait for 5 seconds before publishing the next data

# Start generating sensor data
generate_sensor_data()
