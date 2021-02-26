from django.db import models
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class gov (models.Model):
    gov_name=   models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.gov_name) 
class products (models.Model):
    Productname=   models.CharField(max_length=50)
    def __str__(self):
        return str(self.Productname)       
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

class registry (models.Model):
    registry=   models.CharField(max_length=50,unique=True)
    Factory_ID=models.ForeignKey(Factory, to_field='Factory_ID',db_column='Factory_ID' ,related_name='my', on_delete=models.CASCADE)
    registry_number=models.CharField(max_length=50)
    def __str__(self):
        return str(self.registry_number)
class unit (models.Model):
    unit_name=   models.CharField(max_length=50)
    def __str__(self):
        return str(self.unit_name) 
class Fact_product(models.Model):
    Factory_ID=models.ForeignKey(Factory, on_delete=models.CASCADE,null=True,blank=True)
    product_ID=models.ForeignKey(products, on_delete=models.CASCADE,null=True,blank=True,related_name="t")
    Productq=   models.CharField(max_length=50)
    units_id=models.ForeignKey(unit  ,related_name='ty', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Productq)
       
    class Meta:
        ordering = ["product_ID"] 

 
