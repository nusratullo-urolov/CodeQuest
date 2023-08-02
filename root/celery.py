from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
# "sample_app" is name of the root app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('celery_app',
             broker='amqp://guest:guest@localhost:5672/',
             )

app.autodiscover_tasks()