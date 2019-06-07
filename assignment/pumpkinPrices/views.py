from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PumpkinSerializer
from .models import Pumpkin
from . import forms
from rest_framework.renderers import TemplateHTMLRenderer
import datetime
class CreateView(generics.ListAPIView):
	queryset = Pumpkin.objects.all()
	serializer_class = PumpkinSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class PumpkinFormResult(APIView):
	"""
	Used to display prices for chosed city,variety,dates
	"""
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'pumpkinPrices/pumpkin_form_result.html'

	def get(self, request):
		city = self.request.query_params.get('city', None)
		variety = self.request.query_params.get('variety', None)
		date = self.request.query_params.get('date', None)	

		queryset = Pumpkin.objects.filter(city=city, variety=variety, date=date)
		serializer = PumpkinSerializer(queryset, many=True)
	# serialized_data = self.get_paginated_response(serializer.data)
		return Response({"Pumpkins": queryset})


class PumpkinFormBeforeResult(APIView):
	"""
	Show the last 30 day highest and lowest from that day
	"""
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'pumpkinPrices/pumpkin_form_result.html'

	def get(self, request):
		city = self.request.query_params.get('city', None)
		variety = self.request.query_params.get('variety', None)
		Dt = self.request.query_params.get('date', None)	

		queryset = Pumpkin.objects.filter(city=city, variety=variety, date__gte=datetime.datetime.strptime(Dt, "%Y-%m-%d").date()-datetime.timedelta(days=30))
		queryset = queryset.filter(date__lte=Dt)
		serializer = PumpkinSerializer(queryset, many=True)
	# 	serializer = PumpkinSerializer(queryset, many=True)
	# serialized_data = self.get_paginated_response(serializer.data)
			# return Response({"Pumpkins": queryset})
		return Response({"Pumpkins": queryset})	

def pumpkin_form_view(request):
	form = forms.PumpkinForm()
	return render(request, 'pumpkinPrices/pumpkin_form.html',{'form':form})

class DetailsView(APIView):
	"""
	Same view as PumpkinFormResult but not bound to a form, so can be used for other
	"""
	# serializer_class = PumpkinSerializer
	#POST provides data in request.data, can use this also in GET: Not recommended
	#GET provides data in request.query_params or request.GET.get('') {some.site.com/pumpkins?city=...}
	def get(self,request):
		
		queryset = Pumpkin.objects.all()
		city = self.request.query_params.get('city', None)
		variety = self.request.query_params.get('variety', None)
		date = self.request.query_params.get('date', None)	

		if city is not None and variety is not None and date is not None: 
			queryset = queryset.filter(city=city, variety=variety, date=date)
			serializer = PumpkinSerializer(queryset, many=True)
			# serialized_data = self.get_paginated_response(serializer.data)
			return Response({"Pumpkins": serialized.data})
		else:
			serializer = PumpkinSerializer(queryset, many=True)
			# serialized_data = self.get_paginated_response(serializer.data)
			return Response({"Pumpkins": serializer.data})
