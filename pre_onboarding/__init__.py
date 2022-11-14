# This will make sure the app is always imported when
# Django starts so that the shared_task will use this app
from .task import app as celery_app

__all__ = ('celery_app', )