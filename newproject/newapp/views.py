from django.shortcuts import render
from .models import leave_application



def main(request):
    return render(request, 'main.html')


def manager(request):
    return render(request, 'manager.html')

def employee(request):
    return render(request, 'employee.html')

def logout(request):
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def viewapp(request):
    applications = leave_application.objects.all()
    return render(request, 'application.html', {'applications': applications})



def addleaveapp(request):
    if request.method == 'POST':
        lemployee_ID = int(request.POST['lemployee_ID'])
        leave_type_id = int(request.POST['leave_type_id'])
        date_of_application = request.POST['date_of_application']
        l_from = request.POST['l_from']
        l_to = request.POST['l_to']
        no_of_days = int(request.POST['no_of_days'])
        reason = request.POST['reason']
        approval_status = request.POST['approval_status']
        new_application = leave_application(lemployee_ID_id=lemployee_ID, approval_status=approval_status, leave_type_id_id=leave_type_id,date_of_application=date_of_application,no_of_days=no_of_days, l_from=l_from, l_to=l_to, reason=reason)
        new_application.save()

    elif request.method == 'GET':
        return render(request, 'addleaveapp.html')