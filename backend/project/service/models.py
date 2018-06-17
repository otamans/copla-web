from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField()
    date = models.DateTimeField()
    provide = models.BooleanField()
