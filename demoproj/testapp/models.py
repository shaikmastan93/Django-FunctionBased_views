from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
        
