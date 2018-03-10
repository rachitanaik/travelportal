from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>Employee</h1>')

# Create your views here.
