from django.db import models

# Create your models here.
class book(models.Model):
    nameofbook = models.CharField(max_length=200)
    statusofbook = models.CharField(max_length=200)
    rollnoburrower=models.IntegerField()
