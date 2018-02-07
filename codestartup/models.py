from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Place(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='places', blank=True)
    user = models.ForeignKey(User)


    def __str__(self):
        return self.title
