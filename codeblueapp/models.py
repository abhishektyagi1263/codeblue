from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=256,unique = True)
