from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
