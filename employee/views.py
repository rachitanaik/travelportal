from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import TravelForm,Employee,TravelDetails,ExpenseForm, ExpenseDetails
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def details(request):
	
	return render(request,'employee/details.html',{})


def viewtravelform(request):
	try:
		tr_dets_all = TravelDetails.objects.all()
	except TravelDetails.DoesNotExist:
		raise Http404("Travel Details Do Not Exist")
	context = {
	    'tr_dets_all':tr_dets_all
	}
	return render(request, 'employee/view_tr.html', context)

def viewexpenseform(request):
	try:
		e_dets_all = ExpenseDetails.objects.all()
	except ExpenseDetails.DoesNotExist:
		raise Http404("Expense Details Do Not Exist")
	context = {
	    'e_dets_all':e_dets_all
	}
	return render(request, 'employee/view_ed.html', context)


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


def viewexpenseformfiles(request,receipt):
	return redirect("http://127.0.0.1:8000/media/<receipt>/")



def expenseform(request):
	emp1 = get_object_or_404(Employee,pk=1)
	t2 = ExpenseDetails()

	if request.method=='POST' :
	 form_class = ExpenseForm(request.POST,request.FILES)
	 if form_class .is_valid():
	 	t2.employee = emp1
	 	t2.expense_title = form_class.cleaned_data['expense_title']
	 	t2.category = form_class.cleaned_data['category']
	 	t2.date = form_class.cleaned_data['date']
	 	t2.amount = form_class.cleaned_data['amount']
	 	t2.receipt = form_class.cleaned_data['receipt']
	 	t2.save()

	 else:
	  	return HttpResponse('<h1>Invalid Expense Request</h1>')


	 return HttpResponseRedirect(reverse('details') )
	else:
		form_class = ExpenseForm()
	return render(request, 'employee/expense.html', {'form' :form_class,})




# Create your views here.
