from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    
class Signup(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    