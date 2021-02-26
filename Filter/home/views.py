from django.shortcuts import render
from django.views import View
from django.conf import settings
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from .filters import FactoryFilter
from .models import Factory
from django_filters.views import FilterView


class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/index.html', context)
class FilteredFactoryListView(SingleTableMixin, FilterView,ExportMixin):
    model =Factory
    filterset_class = FactoryFilter
    #context_object_name = 'users'  # Default: object_list
    paginate_by = 1



''' {% autopaginate f.qs 40 as filter_list %}

    {% for obj in filter_list %}
        {{ obj.name }} - ${{ obj.price }}<br />
    {% endfor %} 
    {% paginate %}
    '''