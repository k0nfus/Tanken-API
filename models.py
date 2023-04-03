from django.db import models
from django.urls import reverse
import datetime

class Tanken(models.Model):
    betrag = models.DecimalField(max_digits=7, decimal_places=2)
    datum = models.DateField(default=datetime.date.today, editable=True)
    bemerkung = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural="Tankvorgänge"

    def __str__(self):
        return "Datum: {}, Betrag: {} €".format(self.datum, self.betrag,)
    
    def get_absolute_url(self):
        return reverse("tanklist")