from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>Vendor</h1>')

# Create your views here.
