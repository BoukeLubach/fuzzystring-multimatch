from django.db import models

# Create your models here.




class MeasurementTag(models.Model):
    MEASUREMENT_TYPES = (
        ('flow', 'Flow'),
        ('temp', 'Temperature'),
        ('pres', 'Pressure'),
        ('pwr', 'Power'),
        ('level','Level'),
        ('oth', 'Other'),
    )

    tagName = models.CharField(max_length=124)
    description = models.CharField(max_length=124)
    uom = models.CharField(max_length=124, blank=True, null=True)
    site = models.CharField(max_length=124, blank=True, null=True)
    company = models.CharField(max_length=124, blank=True, null=True)
    measurement_type = models.CharField(max_length=5, choices=MEASUREMENT_TYPES, default='oth')
    
    def __str__(self):
        return(self.tagName)
