# views.py
from django.http import JsonResponse
from rest_framework import status
from .serializers import FileSerializer
from .tasks import create_file_task
# from django.contrib.auth import authenticate, login
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework.views import APIView

class CreateFileView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            create_file_task.delay(username, serializer.data['name'], serializer.data['data'])
            return JsonResponse({'message': 'Файл создан'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)