from django.db import models

# Create your models here.
class Cat(models.Model):
                #  specify filed bcz it choose random
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
