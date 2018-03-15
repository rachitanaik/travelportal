from django.db import models
from django import forms

class approval(forms.Form):
	approval = forms.CharField(label = 'Confirm or Ask For Clarification:', required = True)



# Create your models here.
