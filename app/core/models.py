from django.db import models

class Person(models.Model):
    file = models.FileField()
    