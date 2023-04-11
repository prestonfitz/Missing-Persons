# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

from django.db import models
from datetime import datetime

# Create your models here.

class missingPersons(models.Model):

    date_missing = models.DateField(default=datetime.today, blank=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    age_at_missing = models.IntegerField(default=0)
    city = models.CharField(max_length=16)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=1)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name) 
