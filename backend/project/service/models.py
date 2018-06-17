from django.db import models

from project.mauth.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=128)


class Service(models.Model):
    owner = models.ForeignKey(Profile, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    photo = models.ImageField()
    date = models.DateTimeField()
    provide = models.BooleanField()


STATUS_CHOICES = (
    ('open', 'OPEN'),
    ('closed', 'CLOSED'),
)


class Work(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default='open')
    worker = models.ManyToManyField(Profile)
    status = models.CharField(choices=STATUS_CHOICES, max_length=8)
    feedback = models.TextField()
