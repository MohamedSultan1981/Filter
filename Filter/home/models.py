from django.db import models
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class products (models.Model):
    Productname=   models.CharField(max_length=50)
    def __str__(self):
        return str(self.Productname)       
class Factory(models.Model):
    
    Factory_Name=models.CharField(max_length=500,verbose_name="اسم المنشأه",null=True,blank=True)
    Factory_ID=models.CharField(max_length=40 ,primary_key=True,verbose_name="رقم السجل")
    Factory_Address=models.TextField(max_length=500,verbose_name="العنوان",null=True,blank=True)
    Factory_Manger=models.CharField(max_length=100,verbose_name="المدير",null=True,blank=True)
    Mobile_number=models.CharField(max_length=12,verbose_name="رقم الموبايل",null=True,blank=True)
    #products=models.ManyToManyField('products',through="Fact_product",verbose_name="المنتجات",null=True,blank=True)
    
    def Productquantities(self):
        return Fact_product.objects.filter(Factory_ID=self.pk).order_by("product_ID")
        #return Fact_product.objects.filter(Factory_ID=self.pk, product_ID__in= self.products.pk)
    def __str__(self):
        return str(self.Factory_ID) 

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

 
