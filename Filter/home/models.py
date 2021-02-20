from django.db import models
from django.core import validators
# Create your models here.
class Factory(models.Model):
    
    Factory_Name=models.CharField(max_length=500)
    Factory_ID=models.CharField(max_length=20 ,primary_key=True)
    Mobile_number=models.CharField(max_length=12,validators=[validators.MinValueValidator(11,message="please enter avalid mobile ")]
    Factory_Address=models.AddressField(max_length=500)
    Factory_city=models.CharField(max_length=50)
    Factory_gov=models.CharField(max_length=50)
    Factory_Manger=models.CharField(max_length=100)
    Factory_Activity=models.CharField(max_length=100)
    def __str__(self):
        return str(self.Factory_ID) 