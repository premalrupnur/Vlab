from django.db import models
from django.db.models.enums import TextChoices
from django.db.models.fields import TextField

# Create your models here.
class procedures(models.Model):
    header = models.TextField()
    list_items = models.TextField()