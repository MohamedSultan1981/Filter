from django.db import models
from django.core import validators

# Create your models here.


class INDUSTRIAL_PRODUCTS(models.Model):
    
    PRODUCT_ID = models.IntegerField(primary_key=True)
    PRODUCT_TITLE = models.CharField(max_length=1000, null = True,blank=True,verbose_name="اسم المنتج")
    
    def __str__(self):
        return str(self.PRODUCT_TITLE) 
    class Meta:
        ordering=('PRODUCT_TITLE', )
        db_table = r'"IDA"."INDUSTRIAL_PRODUCTS"'  
class FACILITY_DATA(models.Model):
    
    FACILITY_ID = models.CharField(max_length=1000,primary_key=True)
    NAME = models.CharField(max_length=100, null = True,blank=True,verbose_name="اسم المنشأه")
    CEO_NAME= models.CharField(max_length=200, null = True,blank=True,verbose_name="المدير")
    DETAILED_ADDRESS=models.CharField(max_length=200, null = True,blank=True,verbose_name="العنوان")
    PRIMARY_MOBILE=models.CharField(max_length=100, null = True,blank=True,verbose_name="الموبايل")
    Prouducts = models.ManyToManyField(INDUSTRIAL_PRODUCTS, through='FACILITY_PRODUCTS',verbose_name="المنتجات")
    def __str__(self):
        return str(self.NAME) 
    def Productquantities(self):
        return FACILITY_PRODUCTS.objects.filter(FACILITY_ID=self.pk).order_by("PRODUCT_ID")
        #return FACILITY_PRODUCTS.objects.filter(Factory_ID=self.pk, PRODUCT_ID__in= self.Prouducts.pk)
    class Meta:

        db_table = r'"IDA"."FACILITY_DATA"'

 class INDUSTRIAL_PRODUCTS(models.Model):
        
    REGISTRY_ID = models.IntegerField(primary_key=True)
    PRODUCT_TITLE = models.CharField(max_length=1000, null = True,blank=True,verbose_name="اسم المنتج")
    
    def __str__(self):
        return str(self.PRODUCT_TITLE) 
    class Meta:
        ordering=('PRODUCT_TITLE', )
        db_table = r'"IDA"."INDUSTRIAL_PRODUCTS"'  


class FACILITY_PRODUCTS(models.Model):
    FACILITY= models.ForeignKey(FACILITY_DATA,on_delete=models.CASCADE)
    PRODUCT= models.ForeignKey(INDUSTRIAL_PRODUCTS,on_delete=models.CASCADE)
    UNIT_ID = models.IntegerField()
    PRODUCT_QUANTITY = models.DecimalField( max_digits=38, decimal_places=3)

    
    def __str__(self):
        return str(self.UNIT_ID) 
       
    class Meta:

        db_table = r'"IDA"."FACILITY_PRODUCTS"'