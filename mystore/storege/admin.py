from django.contrib import admin

# Register your models here.
from .models import Storege, Order, Merchandise


admin.site.register(Storege)
admin.site.register(Order)
admin.site.register(Merchandise)
