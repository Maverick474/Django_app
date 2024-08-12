from django.db import models

# Create your models here.
class DataPoint(models.Model):
    visits = models.JSONField()
    labels = models.JSONField()