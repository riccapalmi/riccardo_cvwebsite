from tracemalloc import start
from django.db import models
import datetime

# Create your models here.
class cvelement(models.Model):
    nome=models.CharField(max_length=60, default=None)
    riassunto=models.CharField(max_length=60, default=None)
    descrizione=models.CharField(max_length=500, default=None) 
    start = models.DateField(("Date"), default=datetime.date.today)
    end = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.nome