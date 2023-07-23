from django.db import models

# Create your models here.

class User(models.Model):
    Ism = models.CharField(max_length=60)
    Familya = models.CharField(max_length=60)
    Telefon = models.CharField(max_length=30)
    Fan=models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Ism

class Fanlar(models.Model):
    Fan = models.CharField(max_length=60)

    def __str__(self):
        return self.Fan