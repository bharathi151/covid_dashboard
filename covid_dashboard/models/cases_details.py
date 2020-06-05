from django.db import models
from .mandal import Mandal
# Create your models here.
class CasesDetails(models.Model):
    confirmed_cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered_cases = models.IntegerField()
    date = models.DateField()
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE,
                               related_name="casesdetails")
