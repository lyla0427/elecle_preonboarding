import time
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pre_onboarding.settings')

app = Celery('pre_onboarding')

# Using a string here means the worker doesn't have to serialize
# the configureation object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#    should have a 'CELERY_' prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()

@app.task
def print_hello():
    time.sleep(10)
    return 'Thank You'