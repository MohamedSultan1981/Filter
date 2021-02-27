from .models import FACILITY_DATA
from django import forms
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
""" class FactoryFilter(django_filters.FilterSet):
    Factory_ID: django_filters.CharFilter(label="hello")

    class Meta:
        model = Factory
        fields = {'Factory_Name':['in']
        , 'Factory_ID':['in']
        , 'Factory_Activity':['in'],'Factory_gov':['in'],'phone_number':['in']}
        
      
        widgets = {
            'phone_number': 'PhoneNumberInternationalFallbackWidget',
            
        }
        """

class FACILITY_DATAFilter(django_filters.FilterSet):
    NAME = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FACILITY_DATA
        fields = ['NAME','CEO_NAME','DETAILED_ADDRESS','PRIMARY_MOBILE','Prouducts',]