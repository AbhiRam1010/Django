from django.db import models

# Create your models here.
class Emp(models.Model):
    ename = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    un=models.CharField( max_length=50)
    pw=models.CharField(max_length=50)


    def __str__(self):
        return self.ename
