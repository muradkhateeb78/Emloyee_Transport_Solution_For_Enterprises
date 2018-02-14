from django.db import models
class abbasi(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField