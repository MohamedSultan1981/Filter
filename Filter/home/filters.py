from .models import Factory
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
  

    
    class Meta:
        model = Factory
        fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number',]
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }