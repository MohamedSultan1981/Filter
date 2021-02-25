from .models import Factory,FACILITY_DATA
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
  

    
    class Meta:
        model = Factory
        fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number',]
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }
class FACILITY_DATAFilter(django_filters.FilterSet):
    NAME = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FACILITY_DATA
        fields = ['NAME','CEO_NAME','DETAILED_ADDRESS','PRIMARY_MOBILE','Prouducts']