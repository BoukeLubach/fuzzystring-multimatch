from django.shortcuts import render
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .models import MeasurementTag
from tsData.forms import FilterForm
from django.views.generic import TemplateView
from fuzzywuzzy import fuzz, process
from django.views.generic.edit import FormView, CreateView

CHOICEFIELD_OPTIONS = (
        'Flow',
        'Temperature',
        'Pressure',
        'Power',
        'Level',
        'Other',
    )

def is_valid_queryparam(param):
    return param != '' and param is not None


def compositeMatch(matchratios):
    cumulativeMatch = 0

    for mr in matchratios:
        cumulativeMatch = cumulativeMatch + (mr/100)**4
        
    
    compositeMatch = cumulativeMatch**0.25*100

    return compositeMatch

def calc_match(request, search_query):
  
    queryset = MeasurementTag.objects.all()
    
    for item in queryset:
        tagName = str(item.tagName)
        description = str(item.description)
        site = str(item.site)

        measurement_type = str(item.measurement_type)

        item.nameMRpart = fuzz.partial_ratio(search_query.lower(), tagName.lower())
        item.descMRpart = fuzz.partial_ratio(search_query.lower(), description.lower())
        item.siteMRpart = fuzz.partial_ratio(search_query.lower(), site.lower())
        item.measMRpart = fuzz.partial_ratio(search_query.lower(), measurement_type.lower())
        
        item.nameMRsort = fuzz.token_sort_ratio(search_query.lower(), tagName.lower())
        item.descMRsort = fuzz.token_sort_ratio(search_query.lower(), description.lower())
        item.siteMRsort = fuzz.token_sort_ratio(search_query.lower(), site.lower())
        item.measMRsort = fuzz.token_sort_ratio(search_query.lower(), measurement_type.lower())
        
        item.compositeMR = compositeMatch([item.nameMRpart, item.descMRpart, item.siteMRpart, item.measMRpart])

    return queryset




def tagfilter(queryset, threshold):
    
    for item in queryset:

        if item.compositeMR < int(threshold):           
            queryset = queryset.exclude(id = item.id )


    return queryset

class FilterView(TemplateView):
    template_name = 'tsData/filterform.html'

    def get(self, request):
        
        form = FilterForm(request.GET)

        search_query = request.GET.get('searchInput')
        threshold_value = request.GET.get('filter_threshold')

        if is_valid_queryparam(search_query):
            qs = calc_match(request,search_query)
            qs = tagfilter(qs, threshold_value)
        else:
            qs = MeasurementTag.objects.all()
            
            threshold_value = 85
        

        context = {
            'queryset': qs,
            'choicefield_options': CHOICEFIELD_OPTIONS,
            'form':form,
            'threshold_value': threshold_value,
        }
        
        return render(request, self.template_name, context=context)

