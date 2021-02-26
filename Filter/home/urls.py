from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django_filters.views import FilterView
from .filters import FactoryFilter
urlpatterns = [
    path('', views.FilteredFactoryListView.as_view(), name='search'),
]
