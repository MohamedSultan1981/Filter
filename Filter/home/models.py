from django.db import models
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
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
    FACILITY_DATA_ID=  models.CharField(max_length=5,unique=True ,verbose_name="رقم المنشأه")
    def __str__(self):
        return str(self.NAME) 
    class Meta:
        ordering=('FACILITY_ID', )

        db_table = r'"IDA"."FACILITY_DATA"'

 


class FACILITY_PRODUCTS(models.Model):
    FAC_PROD_ID = models.CharField(max_length=50,primary_key=True)
    FACILITY= models.ForeignKey(FACILITY_DATA,on_delete=models.CASCADE)
    PRODUCT= models.ForeignKey(INDUSTRIAL_PRODUCTS,on_delete=models.CASCADE)
    UNIT_ID = models.IntegerField()
    PRODUCT_QUANTITY = models.DecimalField( max_digits=38, decimal_places=3)

    
    def __str__(self):
        return str(self.UNIT_ID) 
       
    class Meta:
        
        db_table = r'"IDA"."FACILITY_PRODUCTS"'
    

class INDUSTRIAL_REGISTRY(models.Model):
    REGISTRY_ID=models.CharField(max_length=50,primary_key=True)
    FACILITY_DATA_ID=models.OneToOneField(FACILITY_DATA,to_field="FACILITY_DATA_ID", db_column="FACILITY_DATA_ID",on_delete=models.CASCADE)
    
    REGISTRY_NUMBER = models.CharField(max_length=100, null = True,blank=True,verbose_name="رقم السجل")
    
    def __str__(self):
        return str(self.REGISTRY_NUMBER) 
       
    class Meta:
        
        db_table = r'"IDA"."INDUSTRIAL_REGISTRY"'   