from kafka import KafkaProducer
import json
import time
import random

# Initialize the producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

id = 0

# Function to send messages
def send_message(topic, message):
    producer.send(topic, message)
    producer.flush()
    print(f'Sent: {message}')

# Send a message

while True:
    send_message('my-topic', {'key': id})
    id += 1
    time.sleep(1)
