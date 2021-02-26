from django.contrib import admin
from .models import Factory,gov,registry,Fact_product,products,unit
# Register your models here.
admin.site.register(Factory)
admin.site.register(gov)
admin.site.register(registry)
admin.site.register(products)
admin.site.register(Fact_product)
admin.site.register(unit)
