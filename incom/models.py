from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    goo_uid = models.CharField(max_length=150)
    
