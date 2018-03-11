from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import TravelForm,Employee,TravelDetails
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def details(request):
	
	return render(request,'employee/details.html',{})

def travelform(request):
	emp1 = get_object_or_404(Employee,pk=1)
	t1 = TravelDetails()

	if request.method=='POST' :
	 form_class = TravelForm(request.POST)
	 if form_class .is_valid():
	 	t1.employee = emp1
	 	t1.tour_type = form_class.cleaned_data['tour_type']
	 	t1.tour_id = form_class.cleaned_data['tour_id']
	 	t1.source = form_class.cleaned_data['source']
	 	t1.destination = form_class.cleaned_data['destination']
	 	t1.from_date = form_class.cleaned_data['from_date']
	 	t1.to_date = form_class.cleaned_data[ 'to_date']
	 	t1.advance_amount = form_class.cleaned_data['advance_amount']
	 	t1.save()

	 else:
	  	return HttpResponse('<h1>Invalid Travel Request</h1>')


	 return HttpResponseRedirect(reverse('details') )
	else:
		form_class = TravelForm()
	return render(request, 'employee/travelrequest.html', {'form' :form_class,})


def reimbursementform(request):
	return render(request,'employee/reimbursement.html',{})





# Create your views here.
