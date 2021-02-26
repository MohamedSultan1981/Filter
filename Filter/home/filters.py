from .models import Factory
import django_filters
from django_filters.widgets import CSVWidget
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
  

    my__reg=django_filters.CharFilter(lookup_expr='in',label="رقم السجل")
    class Meta:
        model = Factory
        fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number','my__reg']
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }
       