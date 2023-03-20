from tkinter import CASCADE
from django.contrib.gis.db import models

from fields.models import Field

class TechLine(models.Model):
    
    TYPE_CHOICES = [
        ('ABLine','ABLine')
    ]
    
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    heading = models.DecimalField(max_digits=18, decimal_places=15)
    aPoint = models.PointField()
    bPoint = models.PointField()
    lastModifiedTime = models.DateTimeField(auto_now=True)
    archived = models.BooleanField()

    field = models.ForeignKey(Field, on_delete=models.CASCADE)