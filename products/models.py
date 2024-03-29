from django.db import models


class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    img_url=models.CharField(max_length=2083)


class NewOffer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField(max_length=5)
