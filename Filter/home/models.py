from django.db import models
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class gov (models.Model):
    gov_name=   models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.gov_name) 
class Factory(models.Model):
    
    Factory_Name=models.CharField(max_length=500,verbose_name="اسم المنشأه")
    Factory_ID=models.CharField(max_length=20 ,primary_key=True,verbose_name="رقم السجل")
    Factory_Address=models.TextField(max_length=500,verbose_name="العنوان")
    Factory_city=models.CharField(max_length=50,verbose_name="المدينة")
    Factory_gov=models.ForeignKey(gov,on_delete=models.CASCADE,blank=True,null=True,verbose_name="المحافظة")
    Factory_Manger=models.CharField(max_length=100,verbose_name="المدير")
    Factory_Activity=models.CharField(max_length=100,verbose_name="النشاط")
    Mobile_number=models.CharField(max_length=12,verbose_name="رقم الموبايل")
    phone_number = PhoneNumberField(null=True,blank=True,default=None,verbose_name="رقم التليفون")
    def __str__(self):
        return str(self.Factory_ID) 

class address(models.Model):
    
    ADDRESS_TYPE_ID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=50, null = True,blank=True)
    NAME_EN = models.CharField(max_length=25, null = True,blank=True)
    def __str__(self):
        return str(self.NAME) 
    class Meta:
         db_table = "employees"