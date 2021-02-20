from django.db import models
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class gov (models.Model):
    gov_name=   models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.gov_name) 
class Factory(models.Model):
    
    Factory_Name=models.CharField(max_length=500)
    Factory_ID=models.CharField(max_length=20 ,primary_key=True)
    Factory_Address=models.TextField(max_length=500)
    Factory_city=models.CharField(max_length=50)
    Factory_gov=models.ForeignKey(gov,on_delete=models.CASCADE,blank=True,null=True)
    Factory_Manger=models.CharField(max_length=100)
    Factory_Activity=models.CharField(max_length=100)
    Mobile_number=models.CharField(max_length=12)
    phone_number = PhoneNumberField(null=True,blank=True,default=None,)
    def __str__(self):
        return str(self.Factory_ID) 

