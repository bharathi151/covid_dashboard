from django.db import models
from .state import State
# Create your models here.
class District(models.Model):
    district_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE,
                              related_name='districts')
