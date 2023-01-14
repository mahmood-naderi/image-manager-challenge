# REST framework
from rest_framework import serializers

# directories
from .models import User

class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class User_Search_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']
