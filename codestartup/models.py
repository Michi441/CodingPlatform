from django.db import models

# Create your models here.



class Place(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.title
