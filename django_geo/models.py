from django.db import models
ADDRESS_DISPLAY_CHARS = 25

class ZipCode(models.Model):
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=25)
    def __unicode__(self):
        return self.zip_code
