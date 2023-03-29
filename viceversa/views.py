from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	# reauest это параметре, содержащий в себе очень много инфы.
	return HttpResponse("This page name is 'about'")

def home(request):
	# reauest это параметре, содержащий в себе очень много инфы.
	return render(request, 'home.html', {'greeting':'Hello!'})