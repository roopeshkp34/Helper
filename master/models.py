from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kuri(models.Model):
    refer_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    amount = models.FloatField()
    details = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
