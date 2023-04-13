from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('manager', views.manager, name='manager'),
    path('employee', views.employee, name='employee'),
    path('addleaveapp', views.addleaveapp, name='addleaveapp'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('applications', views.viewapp, name='leave-applications')
]