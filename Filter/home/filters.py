from .models import Factory
import django_filters
from django_filters.widgets import CSVWidget
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
  

    my__reg=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text="A list of county names, comma separated")
    class Meta:
        model = Factory

        fields = {'Factory_Name':['in']
        , 'Factory_ID':['in']
        , 'Factory_Activity':['in'],'Factory_gov':['in'],'phone_number':['in'],'my__reg':['in']}
        lables={
          'my__reg':["رقم السجل"]


        }
        #fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number','my__reg']
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }
       