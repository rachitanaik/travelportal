from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>Manager</h1>')

# Create your views here.
