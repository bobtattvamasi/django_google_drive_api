# nova_test_project/celery.py
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nova_test_project.settings')

app = Celery('nova_test_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()