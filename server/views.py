import os
import json
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import MyFileSerializer
from .models import File
from django.http import FileResponse
from rest_framework.decorators import api_view
from django.views.generic.base import View
#from django.views.decorators.http import require_GET

@api_view(['GET'])
def file_list(request):
    file = File.objects.all()
    serializer = MyFileSerializer(file, many = True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def file_upload(request):
    if request.method == 'POST':
        serializer = MyFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.validated_data
            result = []
            traverse(data, result=result)
            output = "\n".join(result)
            path = "output.txt"
            with open(path, "w") as file:
                file.write(output)
            # Return a download response
            response = FileResponse(open(path, 'rb'), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="output.txt"'
            return response
        return Response(serializer.validated_data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def traverse(item, result, path=""):
    if isinstance(item, dict):
        for key, value in item.items():
            traverse(value, result, f'{path}."{key}"')
    elif isinstance(item, list):
        for value in item:
            traverse(value, result, path)
    else:
        result.append(f'{path[1:]}."{item}",')

@csrf_exempt
def index(request):
    if request.method == 'POST' and 'file' in request.FILES:
        upload_file = request.FILES.get('file', None)
        if upload_file is not None:
            data = json.loads(upload_file.read())
            result = []
            traverse(data, result=result)
            output = "\n".join(result)
            path = "output.txt"
            with open(path, "w") as file:
                file.write(output)
            # Return a download response
            response = FileResponse(open(path, 'rb'), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="output.txt"'
            return response
    else:
        return render(request, 'file/index.html')

