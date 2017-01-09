from django.db import models
from django.contrib.auth.models import Permission, User

class MovieInfo(models.Model):
    Name= models.CharField(max_length=250)
    Cast= models.CharField(max_length=250)
    Director= models.CharField(max_length=250)
    Genre= models.CharField(max_length=250)
    Year= models.CharField(max_length=250)
    Plot= models.CharField(max_length=2500, default='')
    Poster= models.CharField(max_length=2500, default='')
    Rating= models.CharField(max_length=25, default='')
    Trailer= models.CharField(max_length=2500, default='')
    Price= models.CharField(max_length=25, default='')

    def __str__(self):
        return self.Name