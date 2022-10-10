from django.db import models
from notices.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(unique=True, max_length=32)
    link = models.CharField(max_length=256)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class TODO(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create = models.TimeField(auto_now_add=True)
    update = models.TimeField(auto_now=True)
    is_active = models.BooleanField
