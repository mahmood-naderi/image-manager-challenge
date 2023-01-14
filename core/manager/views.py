# Third-party
import re
from django_filters.rest_framework import DjangoFilterBackend
# Django
# Directories
from .models import Image
from .serializers import Image_Serializer, Image_Retrieve_Serializer
from users.models import User
from users.serializers import User_Serializer, User_Search_Serializer
# REST framework
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response

class Save_Retrieve_Image(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Image_Serializer
    queryset = Image.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'location', 'created_date']
    search_fields = ['name']

class Retrieve_Image_ID(APIView):
    serializer_class = Image_Retrieve_Serializer

    def get(self, request, pk, *args, **kwargs):
        image = Image.objects.get(id = pk)
        serialized_image = self.serializer_class(image)

        return Response(serialized_image.data, status = status.HTTP_200_OK)


class Search_Username(APIView):
    serializer_class = User_Search_Serializer

    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.filter(username__iregex = rf'^{re.escape(username)}[a-zA-Z1-9]*$').values()
            serialized_user = self.serializer_class(user, many = True)
            return Response(serialized_user.data, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)