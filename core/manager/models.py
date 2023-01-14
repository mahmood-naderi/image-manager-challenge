from django.db import models
from users.models import User

class Location(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    name = models.CharField(max_length = 20)
    location = models.ForeignKey(Location, on_delete = models.SET_NULL, null = True)
    description = models.TextField()
    created_date = models.DateField()
    creator = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


