from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100000, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)

    cost = models.IntegerField()

    size = models.DecimalField(max_digits=100000, decimal_places=2)

    description = models.TextField()

    age_limited = models.BooleanField(default=False)

    buyer = models.ManyToManyField(Buyer)
    def __str__(self):
        return self.title

#Пагинация
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)