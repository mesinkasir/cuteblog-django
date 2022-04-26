from django.db import models
from django.http import HttpResponse

class Post (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    

    def __str__(self) ->str:
        return self.name[:15]