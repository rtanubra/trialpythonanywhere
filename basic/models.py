from django.db import models

# Create your models here.
class Owner(models.Model):
    username = models.CharField(max_length=100, unique =True)
    def __str__(self):
        return self.username
