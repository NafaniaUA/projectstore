from django.db import models
from django.conf import settings 

# Create your models here.
class Storege(models.Model):
    storege_title = models.CharField(max_length=128)
    storege_admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.storege_title

class Merchandise(models.Model):
    
    mercandise_title = models.CharField(max_length=128)
    merchandise_descript = models.CharField(max_length=120)
    merchandise_conect = models.ManyToManyField(Storege, through='Order')
    

    def __str__(self):
        return self.mercandise_title

class Order(models.Model):
    
    order_connect_mer = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    orderr_connect_stor = models.ForeignKey(Storege, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_depart_date = models.DateField()
    order_prepare = models.BooleanField()
    order_depart = models.BooleanField()
