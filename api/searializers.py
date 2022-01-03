from django.db.models import fields
from rest_framework import serializers
from .models import Post,Firmware

class PostSearializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 

class FirmwareSearializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields = '__all__' 