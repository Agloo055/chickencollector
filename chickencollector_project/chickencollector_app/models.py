from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('L', 'Late Afternoon')
)

# Create your models here.
class Chicken (models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.id})
    
class Laying (models.Model):
    date = models.DateField('laying Date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )

    chicken = models.ForeignKey(Chicken, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"