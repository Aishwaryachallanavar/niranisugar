from django.shortcuts import render
from .models import leave_application




def index(request):
    return render(request, 'index.html')



def viewapp(request):
    applications = leave_application.objects.all()
    return render(request, 'application.html', {'applications' : applications})