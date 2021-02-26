from .models import Factory
import django_filters
from django_filters.widgets import CSVWidget
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
  

    my__reg=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text="A list of county names, comma separated")
    class Meta:
        model = Factory

        fields = ['Factory_Name'
        , 'Factory_ID'
        , 'Factory_Activity','Factory_gov','phone_number','products']
        lables={
          'my__reg':["رقم السجل"]


        }
        #fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number','my__reg']
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }
       