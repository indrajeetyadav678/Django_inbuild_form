from django.db import models

# Create your models here.

class RegistrationModel(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField( null=False)
    Number=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Con_Password=models.CharField(max_length=30)
