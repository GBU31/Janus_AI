from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import FileModel
from django.http import FileResponse
import os
import random
import string
from .serializers import FileSerializer

def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, "error.html")

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            os.system(f'python3 main/DeepFake/main.py videos/{str(request.data["video"])} images/{str(request.data["image"])} output/{random_string}.avi')
            response = FileResponse(open('output/'+random_string + '.avi', 'rb'))
            response['Content-Disposition'] = f'attachment; filename=output/"{random_string}.avi"'
            os.system(f'rm -rf videos/{str(request.data["video"])} images/{str(request.data["image"])} output/{random_string}.avi')
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
