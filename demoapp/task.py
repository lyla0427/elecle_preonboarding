import time, random
from celery import shared_task

@shared_task
def print_hello(user):
    time.sleep(random.randint(1, 5))
    return print('hello')