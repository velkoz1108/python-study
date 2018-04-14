from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    creator = models.CharField(max_length=20)
    modifier = models.CharField(max_length=20)


class proft(models.Model):
    name = models.CharField(max_length=20)
    per = models.CharField(max_length=20)
    cdn = models.CharField(max_length=5,default='222')
    is_new = models.BooleanField(default=bool)