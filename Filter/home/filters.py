from .models import Factory
import django_filters

class FactoryFilter(django_filters.FilterSet):
    class Meta:
        model = Factory
        fields = ['Factory_Name', 'Factory_ID', 'Factory_Activity', ]