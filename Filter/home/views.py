from django.shortcuts import render
from django.views import View
from django.conf import settings
from .models import Factory,FACILITY_DATA
from .filters import FactoryFilter,FACILITY_DATAFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin


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

class FilteredFACILITY_DATAListView(SingleTableMixin, FilterView,ExportMixin):
    model =FACILITY_DATA
    filterset_class=FACILITY_DATAFilter