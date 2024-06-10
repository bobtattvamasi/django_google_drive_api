from django.urls import path
from . import views  # Import your app's views.py

urlpatterns = [
    path('create-file/', views.CreateFileView.as_view(), name='create_file'),
]