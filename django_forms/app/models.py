from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    add = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    cource = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    