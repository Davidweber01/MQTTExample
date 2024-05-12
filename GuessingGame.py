import paho.mqtt.client as mqtt
import random

# MQTT broker address and port
broker_address = "ea-pc165.ei.htwg-konstanz.de"
broker_port = 1883

# MQTT topic to publish to
topic = "/SysArch/test/#"

# Message to send
message = "Hello, MQTT!, from Python"

# MQTT username and password
mqtt_username = "V5"
mqtt_password = "DE9"

# MQTT client setup
client = mqtt.Client()

# Set username and password
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Connect to the MQTT broker
client.connect(broker_address)

# Generate a random number between 0 and 1000
secret_number = random.randint(0, 1000)
print("Secret number generated.")


# Function to handle incoming messages
def on_message(client, userdata, message):
    name = message.topic.split("/")[-1]


    try:
        guess = int(message.payload.decode())
        if guess == secret_number:
            print(f"Congratulations {name}! You guessed the correct number.")
            client.disconnect()
        elif guess < secret_number:
            print(f"{name}:{guess} is too small! Try again.")
        else:
            print(f"{name}:{guess} is too large! Try again.")

    except:
        print("Input wasn't a number!")


client.on_message = on_message

# Subscribe to the topic
client.subscribe(topic)

# Loop indefinitely to receive messages
client.loop_forever()
