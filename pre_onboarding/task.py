import time
from celery import shared_task

@shared_task
def print_hello(user):
    time.sleep(10)
    return print('Thank You')


@shared_task
def add(x, y):
    return x+y