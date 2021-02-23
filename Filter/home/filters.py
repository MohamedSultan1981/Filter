from .models import Factory,address
from django import forms
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
    Factory_ID: django_filters.CharFilter(label="hello")

    class Meta:
        model = Factory
        fields = {'Factory_Name':['in']
        , 'Factory_ID':['in']
        , 'Factory_Activity':['in'],'Factory_gov':['in'],'phone_number':['in']}
        
      
        widgets = {
            'phone_number': 'PhoneNumberInternationalFallbackWidget',
            
        }
       

class addressFilter(django_filters.FilterSet):
    

    class Meta:
        model = address
        fields = ['NAME']