import pika
import time


conn=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan=conn.channel()
chan.queue_declare(queue='first_queue')


def callback(ch,method,properties,body):
    print(" [x] Сообщение получено %r" % (body,))
    time.sleep(body.count(b'.'))
    print('Готово')

chan.basic_consume(on_message_callback=callback, queue='first_queue', auto_ack=True)
print(" [*] Ожидание сообщений. Для выхода идите в окно")
chan.start_consuming()
