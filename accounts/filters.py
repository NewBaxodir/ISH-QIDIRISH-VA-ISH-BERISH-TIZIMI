import django_filters
from django.forms.widgets import TextInput
from django_filters import CharFilter, ChoiceFilter

from summary.models import Summary
from jobs.models import Vacanciess



class VacanciessFilter(django_filters.FilterSet):
    job_title = CharFilter(field_name='job_title', lookup_expr='icontains', widget=TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Профессия, должность или компания"}))
  
    class Meta:
        model = Vacanciess
        fields = ['job_title',]



class SummaryFilter(django_filters.FilterSet):
    carobjec = CharFilter(field_name='carobjec', lookup_expr='icontains', widget=TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Профессия, должность или компания"}))
  
    class Meta:
        model = Summary
        fields = ['carobjec',]



















