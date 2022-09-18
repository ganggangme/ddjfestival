from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Booth(models.Model):
    name = models.CharField(max_length=200)
    sub_title = models.TextField()
    intro = models.TextField()
    event = ArrayField(
        models.CharField(max_length=100, blank=True),
        size=10,
    )
    location =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='static/image/food')

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=200)
    emoticon = models.ImageField()

    def __str__(self):
        return self.name

class Gongi(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/image/gongi')

    def __str__(self):
        return self.title
