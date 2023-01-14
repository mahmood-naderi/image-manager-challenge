from rest_framework import serializers
from users.serializers import User_Search_Serializer
from .models import Image, Location

class Location_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"

class Image_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"

class Image_Retrieve_Serializer(serializers.ModelSerializer):
    location = Location_Serializer()
    creator = User_Search_Serializer()

    class Meta:
        model = Image
        fields = "__all__"



