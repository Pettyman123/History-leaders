from typing import Any
from django.db import models
from .import views
# Create your models here.

class leaders(models.Model):
    
    LEADER_CHOICES = [
        ("EU","European Leaders"),
        ("IND", "Indian Leaders"),
        ("AS", "Asian Leaders"),
        ("AMC", "American Leaders"),
        ("MYT", "Mythical Leaders"),
    ]
    
    
    name = models.TextField(max_length=200)
    birth = models.DateField(null=True)
    death = models.DateField(null=True)
    link = models.URLField()
    image = models.ImageField(null=True)
    summary = models.TextField()
    leader_choices = models.CharField( max_length=100,choices=LEADER_CHOICES)
    
    
    def __str__(self):
        return self.name