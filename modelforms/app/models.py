from django.db import models

# Create your models here.

class Topic(models.Model):
    topic = models.CharField(primary_key=True, max_length=50)

    
    def __str__(self):
        return self.topic
    

class Website(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    url = models.CharField( max_length=50)
    email= models.EmailField( max_length=254)
    
    def __str__(self) :
        return self.name

class Access(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    author=models.CharField( max_length=50)
    date= models.DateField()
    
    
    def __str__(self):
        return self.author