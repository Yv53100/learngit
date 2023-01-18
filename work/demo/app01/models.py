from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    account = models.CharField(max_length=20)