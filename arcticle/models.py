from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)
    image =  models.ImageField(upload_to='category/images/')

    def __str__(self):
        return self.name

class Arcticle(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='article/images/')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    read = models.BooleanField()
    resume = models.CharField(max_length= 100)
    body = models.TextField()
    def __str__(self):
        return self.title
    
