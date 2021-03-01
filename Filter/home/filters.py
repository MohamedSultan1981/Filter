from .models import Factory
import django_filters
from django_filters.widgets import CSVWidget
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
class FactoryFilter(django_filters.FilterSet):
    Factory_Name = django_filters.CharFilter(lookup_expr='icontains',label="اسم المنشأة")
    Factory_Manger = django_filters.CharFilter(lookup_expr='icontains',label="المدير")
    Factory_Address = django_filters.CharFilter(lookup_expr='icontains',label="العنوان")
    Factory_Address = django_filters.CharFilter(lookup_expr='icontains',label="التليفون")
  

    Factory_ID=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text="قم بادخال ارقام السجل مفصوله ب علامة الترقيم ,")
    class Meta:
        model = Factory

        fields = ['Factory_Name','Factory_ID','Factory_Address','Factory_Manger','Mobile_number']
        
       
        #fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity','Factory_gov','phone_number','my__reg']
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget,
        }
       