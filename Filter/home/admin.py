from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Factory,Fact_product,products,unit
# Register your models here.
@admin.register(Fact_product)
class Fact_productAdmin(ImportExportModelAdmin):
    pass


@admin.register(products)
class productsAdmin(ImportExportModelAdmin):
    pass
@admin.register(unit)
class unitAdmin(ImportExportModelAdmin):
    pass
@admin.register(Factory)
class FactoryAdmin(ImportExportModelAdmin):
    #search_fields = ('name', 'description', 'keyword', )
    pass