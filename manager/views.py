from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from employee.models import TravelForm,Employee,TravelDetails,ExpenseForm, ExpenseDetails
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import approval

def index(request):
	return render(request,'manager/index.html',{})


def reviewtravelform(request):
	try:
		tr_dets_all = TravelDetails.objects.all()
		form_class=approval()
	except TravelDetails.DoesNotExist:
		raise Http404("Travel Details Do Not Exist")
	context = {
	    'tr_dets_all':tr_dets_all,
	    'form':form_class
	}
	if request.method=='POST' :
		tr_dets_all = TravelDetails.objects.all()
		form_class = approval(request.POST)
		if form_class .is_valid():

			 for tr_det in tr_dets_all:
			 	if tr_det.approval==None:
			 		tr_det.approval = form_class.cleaned_data['approval']
			 		tr_det.save()
			 		break
				
		return HttpResponseRedirect(reverse('reviewtravelform'))
		context = {
	    'form':form_class
	    }

	return render(request, 'manager/review_tr.html', context)
def reviewexpenseform(request):
	count=0
	try:
		e_dets_all = ExpenseDetails.objects.all()
		form_class=approval()
	except ExpenseDetails.DoesNotExist:
		raise Http404("Expense Details Do Not Exist")
	context = {
	    'e_dets_all':e_dets_all,
	    'form':form_class
	    }
	if request.method=='POST' :
		
		e_dets_all = ExpenseDetails.objects.all()
		form_class = approval(request.POST)
		if form_class .is_valid():
			for e_det in e_dets_all:
				if  e_det.approval==None:
					e_det.approval = form_class.cleaned_data['approval']
					e_det.save()
					break
				
				
		return HttpResponseRedirect(reverse('reviewexpenseform') )
	
	   
		context = {
	    'form':form_class
	    }
	    
	return render(request, 'manager/review_ed.html', context)



# Create your views here.
