from django import forms
from .models import city_choice, variety_choice 

class PumpkinForm(forms.Form):
	city = forms.ChoiceField(choices = city_choice, label = 'City')
	variety = forms.ChoiceField(choices = variety_choice, label = 'Variety')
	date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], label = 'Date')