from django.db import models
from django.core import validators

# Create your models here.
class gov (models.Model):
    gov_name=   models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.gov_name) 
class Factory(models.Model):
    
    Factory_Name=models.CharField(max_length=500,verbose_name="اسم المنشأه")
    Factory_ID=models.CharField(max_length=20 ,primary_key=True,verbose_name="رقم المصنع")
    Factory_Address=models.TextField(max_length=500,verbose_name="العنوان")
    Factory_city=models.CharField(max_length=50,verbose_name="المدينة")
    Factory_gov=models.ForeignKey(gov,on_delete=models.CASCADE,blank=True,null=True,verbose_name="المحافظة")
    Factory_Manger=models.CharField(max_length=100,verbose_name="المدير")
    Factory_Activity=models.CharField(max_length=100,verbose_name="النشاط")
    Mobile_number=models.CharField(max_length=12,verbose_name="رقم الموبايل")
    phone_number = PhoneNumberField(null=True,blank=True,default=None,verbose_name="رقم التليفون")
    products=models.ManyToManyField('products',through="Fact_product",verbose_name="المنتجات")
    
    def Productquantities(self):
        return Fact_product.objects.filter(Factory_ID=self.pk).order_by("product_ID")
        #return Fact_product.objects.filter(Factory_ID=self.pk, product_ID__in= self.products.pk)
    def __str__(self):
        return str(self.Factory_ID) 

class INDUSTRIAL_PRODUCTS(models.Model):
    
    PRODUCT_ID = models.IntegerField(primary_key=True)
    PRODUCT_TITLE = models.CharField(max_length=1000, null = True,blank=True,verbose_name="اسم المنتج")
    
    def __str__(self):
        return str(self.PRODUCT_TITLE) 
    class Meta:
        
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
        return FACILITY_PRODUCTS.objects.filter(FACILITY_ID=self.pk).order_by("product_ID")
    class Meta:

        db_table = r'"IDA"."FACILITY_DATA"'

 


class FACILITY_PRODUCTS(models.Model):
    FACILITY= models.ForeignKey(FACILITY_DATA,on_delete=models.CASCADE)
    PRODUCT= models.ForeignKey(INDUSTRIAL_PRODUCTS,on_delete=models.CASCADE)
    UNIT_ID = models.IntegerField()
    PRODUCT_QUANTITY = models.DecimalField( max_digits=38, decimal_places=3)

    
    def __str__(self):
        return str(self.UNIT_ID) 
       
    class Meta:

        db_table = r'"IDA"."FACILITY_PRODUCTS"'