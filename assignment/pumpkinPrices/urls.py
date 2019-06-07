from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views	

urlpatterns = [
	path('pumpkins/api', views.DetailsView.as_view(), name='details'),
	path('pumpkins/',views.pumpkin_form_view, name='pumpkin_form'),
	path('get/',views.PumpkinFormResult.as_view(), name="pumpkin_form_result"),
	path('get/before/',views.PumpkinFormBeforeResult.as_view(),name='pumpkin_form_before_result')
]

urlpatterns = format_suffix_patterns(urlpatterns)