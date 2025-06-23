from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedback_system.settings')

# Create the Celery app
app = Celery('feedback_system')

# Read config from Django settings, prefix with CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered Django app configs
app.autodiscover_tasks()

app.conf.broker_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
