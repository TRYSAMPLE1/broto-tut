from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
    description = models.TextField()
    