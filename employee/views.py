from django.http import HttpResponse
from django.template import loader
from .models import TravelForm,Employee,TravelDetails
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def details(request):
	
	return render(request,'/employee/details.html',{})

def travelform(request):
	emp1 = get_object_or_404(Employee)

	if request.method=='POST' :
	 form_class = TravelForm(request.POST)
	 if form .is_valid():
	 	tour_type = form.cleaned_data['tour_type']
	 	tour_id = form.cleaned_data['tour_id']
	    source = form.cleaned_data['source' ]
	    destination = form.cleaned_data['destination']
	    from_date = form.cleaned_data['from_date']
	    to_date = form.cleaned_data[ 'to_date']
	    advance_amount = form.cleaned_data['advance_amount']
	    .save()

	 return HttpResponseRedirect(reverse('details') )

    # If this is a GET (or any other method) create the default form.
    else:
        
        form = TravelForm()

    return render(request, '/employee/travelrequest.html', {'form' :form_class,})


def reimbursementform(request):
	return render(request,'/employee/reimbursement.html',{})





# Create your views here.
