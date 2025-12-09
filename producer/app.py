import pika
import time

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    for i in range(5):
        msg = f"Mesaj {i}"
        channel.basic_publish(exchange="", routing_key="test_queue", body=msg)
        print("Gönderildi:", msg)
        time.sleep(1)

    connection.close()

if __name__ == "__main__":
    send_message()
