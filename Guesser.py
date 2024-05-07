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

# MQTT client setup
client = mqtt.Client()

# Set username and password
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Connect to the MQTT broker
client.connect(broker_address)

# Function to handle incoming messages
def on_message(client, userdata, message):
    # Placeholder
    pass

client.on_message = on_message

# Loop indefinitely
while True:
    # Get user input for the guess
    guess = input("Enter your guess (0-1000): ")
    
    # Publish the guess to the topic
    client.publish(topic, guess)

# Disconnect from the broker
client.disconnect()
