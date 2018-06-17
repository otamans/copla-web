from django.db import models

from project.mauth.models import Profile


class Plan(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Service(models.Model):
    owner = models.ForeignKey(Profile, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    photo = models.ImageField()
    date = models.DateTimeField()
    provide = models.BooleanField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plans')
    city = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)



STATUS_CHOICES = (
    ('open', 'OPEN'),
    ('closed', 'CLOSED'),
)

class Work(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default='open')
    worker = models.ManyToManyField(Profile)
    status = models.CharField(choices=STATUS_CHOICES, max_length=8)
    feedback = models.TextField()
