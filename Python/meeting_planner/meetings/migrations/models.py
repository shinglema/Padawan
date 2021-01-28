from django.db import models

class Meeting(models.model):
    titel=models.CharField(max_length=200)
    date=models.DateField()
    