from django.db import models

class User(models.Model):
  name = models.CharField(max_length=25)
  email = models.EmailField(max_length=70)
  password = models.CharField(max_length=10)
