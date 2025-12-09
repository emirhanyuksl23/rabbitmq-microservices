import pika

def callback(ch, method, properties, body):
    print("Tüketildi:", body.decode())

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="test_queue")

channel.basic_consume(queue="test_queue", on_message_callback=callback, auto_ack=True)

print("Consumer çalışıyor...")
channel.start_consuming()
