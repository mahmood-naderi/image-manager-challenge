# Django

# REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

# Directories
from .serializers import User_Serializer

class User_Register(generics.GenericAPIView):
    serializer_class = User_Serializer

    def post(self, request, *args, **kwargs):
        serialized_user = self.serializer_class(data=request.data)

        if serialized_user.is_valid():
            serialized_user.save()
            email = serialized_user.validated_data["email"]
            response_data = {"email": email}

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)




