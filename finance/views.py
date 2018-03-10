from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>Finance</h1>')

# Create your views here.
