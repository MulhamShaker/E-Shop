from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)