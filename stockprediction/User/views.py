from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# Create your views here.
def home_User(request):
	return render(request, 'User/index.html')