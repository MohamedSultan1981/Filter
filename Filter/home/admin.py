from django.contrib import admin
from .models import Factory,gov,reg,Fact_product,products
# Register your models here.
admin.site.register(Factory)
admin.site.register(gov)
admin.site.register(reg)
admin.site.register(products)
admin.site.register(Fact_product)
