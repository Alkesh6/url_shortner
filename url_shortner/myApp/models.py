from django.db import models

# Create your models here.
class url(models.Model):
    long_url = models.URLField(max_length=400)
    short_url = models.CharField(max_length=20,unique=True)
    date_field = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

