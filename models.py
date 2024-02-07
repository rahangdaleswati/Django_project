from django.db import models


class Order(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.FloatField()
    del_date = models.DateField()
    del_address = models.CharField(max_length=40)
    gift_option = models.BooleanField()
    payment_mode = models.CharField(max_length=10)