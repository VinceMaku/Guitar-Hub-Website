try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "index.html")
def about(request):
	return render(request, "about.html")
def acoustic(request):
	return render(request, "acoustic.html")
def electric(request):
	return render(request, "electric.html")
def guitartuner(request):
	return render(request, "guitartuner.html")