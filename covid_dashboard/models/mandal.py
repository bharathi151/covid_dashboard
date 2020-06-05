from django.db import models
from .state import State
from .district import District
# Create your models here.
class Mandal(models.Model):
    mandal_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE,
                               related_name='mandals')
