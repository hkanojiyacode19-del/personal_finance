from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Item_name = models.CharField(max_length=200)
    description = models.TextField()
    Amount = models.CharField(max_length=100) # day
    Date_of_purchase = models.CharField(max_length=100) #
    

    def __str__(self):
        return self.title