from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from . import forms


# Create your models here.

class Patient_info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)

    datecreated=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.phone

    def __str__(self):
        return self.email
