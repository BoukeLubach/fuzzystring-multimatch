from django.urls import path

from .views import (
    FilterView, 

)

urlpatterns = [
    path('tag/search/', FilterView.as_view(), name ='filterFormView'),

]