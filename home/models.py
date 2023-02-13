from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
