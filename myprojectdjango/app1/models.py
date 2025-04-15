from django.db import models


class Users(models.Model):
    name = models.CharField(blank=False)
    surname = models.CharField(blank=False)
    birthdate = models.DateField(default=0)


class Book(models.Model):
    title = models.CharField(blank=False)
    pages = models.IntegerField(default=0)
    