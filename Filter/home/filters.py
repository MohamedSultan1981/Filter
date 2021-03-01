from .models import FACILITY_DATA
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
from .models import FACILITY_DATA,INDUSTRIAL_PRODUCTS

class FACILITY_DATAFilter(django_filters.FilterSet):
    NAME = django_filters.CharFilter(lookup_expr='icontains',label="اسم المنشأة")
    my__REGISTRY_NUMBER=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text="قم بادخال ارقام السجل مفصوله ب علامة الترقيم")
    CEO_NAME=django_filters.CharFilter(lookup_expr='icontains',label="اسم المدير")
   
    class Meta:
        model = FACILITY_DATA
        fields = ['NAME','CEO_NAME','DETAILED_ADDRESS','PRIMARY_MOBILE','my__REGISTRY_NUMBER','Prouducts']
      