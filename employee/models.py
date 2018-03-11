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
	name=models.CharField(max_length = 50)
	designation=models.CharField(max_length = 50)
	phone_no=models.IntegerField(null=True)
	email_id=models.CharField(max_length = 50)

	def __str__(self):
		return self.name
	


class TravelDetails(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
	tour_type = models.CharField(max_length = 50)
	tour_id = models.IntegerField(null=True)
	source = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	from_date = models.DateField(null=True)
	to_date = models.DateField(null=True)
	advance_amount = models.IntegerField(blank=True, null=True)
	



# Create your models here.
