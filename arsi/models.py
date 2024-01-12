from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Product(models.Model):
    product_title=models.CharField(_("title"),max_length=100)
    price=models.CharField(_("price"),max_length=100)
    product_rating=models.FloatField(_("product rating"),blank=True,null=True)
    shipping=models.CharField(_("shipping"),max_length=100)
    seller_rating=models.CharField(_("seller rating"),max_length=100)
    shippping_score=models.CharField(_("shipping score"),max_length=100)
    
    def __str__(self):
        return self.product_title