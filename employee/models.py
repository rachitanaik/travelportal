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

class ExpenseForm(forms.Form):
	
	expense_title = forms.CharField(required=True)
	category = forms.CharField(required=True)
	date = forms.DateField(required=True)
	amount = forms.IntegerField(required=True)
	receipt = forms.FileField(required = False)


class Employee(models.Model):
	name=models.CharField(max_length = 50)
	designation=models.CharField(max_length = 50)
	phone_no=models.IntegerField(null=True)
	email_id=models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class ExpenseDetails(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
	expense_title = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50)
	date = models.DateField(null=True)
	amount = models.IntegerField(null=True)
	receipt = models.FileField(upload_to='media')
	approval = models.CharField(max_length=20,null=True,default='None')
	


class TravelDetails(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
	tour_type = models.CharField(max_length = 50)
	tour_id = models.IntegerField(null=True)
	source = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	from_date = models.DateField(null=True)
	to_date = models.DateField(null=True)
	advance_amount = models.IntegerField(blank=True, null=True)
	approval = models.CharField(max_length=20,null=True,default='None')
	



# Create your models here.
