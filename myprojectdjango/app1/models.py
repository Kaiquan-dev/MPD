from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    birthdate = models.DateField(default=0)

    def __str__(self):
        return f'{self.surname} {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    