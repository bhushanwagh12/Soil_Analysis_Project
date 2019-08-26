from django.db import models

# Create your models here.

class Login(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Email