import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class RegFilter(django_filters.FilterSet):
	class Meta:
		model = Registration
		fields = '__all__'
		exclude = ['student', 'registration_date']