from celery import Celery
from kombu import Exchange, Queue
# import mongoengine
# create function for celery with mongo as backend and rabbitmq with queue name test_queue exchnage type fanout.
# celery = Celery('app', backend='mongodb://localhost:27017/celery', broker='amqp://guest@localhost//', task_routes={'app.tasks.*': {'queue': 'test_queue', 'exchange': 'test_exchange', 'routing_key': 'test_queue'}})
def celery_setup():
    celery = Celery('app', backend='mongodb://localhost:27017/celery', broker='amqp://guest@localhost::5672//', task_routes={
        'app.tasks.*': {'queue': 'test_queue', 'exchange': 'test_exchange', 'routing_key': 'test_queue'}})

    print("Celery")
    return f'{celery} : setup done'

celery_setup()
