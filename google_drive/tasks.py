# google_drive/tasks.py
from celery import shared_task
from .models import File
from .services import create_file_in_google_drive

@shared_task
def create_file_task(user_id, name, data):
    try:
        file = File.objects.create(user=user_id, name=name, data=data)
        create_file_in_google_drive(file)
        return "File created successfully!"
    except Exception as e:
        return "Error creating file in create_file_task(): {}".format(e)