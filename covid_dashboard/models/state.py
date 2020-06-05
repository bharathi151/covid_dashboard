from django.db import models

# Create your models here.
class State(models.Model):
    state_name = models.CharField(max_length=100)
