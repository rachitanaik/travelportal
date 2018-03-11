from django.db import models
from django import forms

class TravelForm(forms.Form):
	tour_type = forms.CharField(label = "Type of Tour :",required=True)
	tour_id = forms.IntegerField(label ="Tour Id",required=True)
	source = forms.CharField(required=True)
	destination = forms.CharField(required=True)
	from_date = forms.DateField(required=True)
	to_date = forms.DateField(required=True)
	advance_amount = forms.IntegerField(required=False)

class Employee(models.Model):
	


class TravelDetails(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	tour_type = models.CharField(max_length = 50)
	tour_id = models.IntegerField()
	source = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	from_date = models.DateField()
	to_date = models.DateField()
	advance_amount = models.IntegerField()
	



# Create your models here.
