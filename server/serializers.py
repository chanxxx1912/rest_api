from rest_framework import serializers
from .models import File


# serializers.py



class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        
        def create(self,data):
            return File.objects.create(**data)
            
