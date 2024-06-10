# google_drive/models.py
from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    '''
        Модель для хранения информации о созданных файлах
    '''
    user = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'google_drive'