# consumer.py
from kafka import KafkaConsumer
import json
import time

# Initialize the consumer
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,
    group_id='my-group'  # Consumer group ID
)

# Function to consume messages
def consume_messages():
    for message in consumer:
        print(f'Received: {message.value}')
        time.sleep(1)

if __name__ == "__main__":
    consume_messages()