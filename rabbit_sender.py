import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.234'))
chan = conn.channel()
chan.queue_declare(queue='first_queue')
message=' '.join(sys.argv[1:]) or "Ничего интересного"
chan.basic_publish(exchange='',
                      routing_key='first_queue',
                      body=message)
print(" [x] Отправлено %r" % (message,))
conn.close()