from django.urls import path
from App import views
from App.views import *


urlpatterns = [
    
    path('addvehicle/', VehicleCreate.as_view(),name='addvehicle'),
    path('vehiclelist/',views.Vehiclelist,name='vehiclelist'),
    path('vehicledelete/<int:id>',views.Vehicledelete,name='Vehicledelete'),
    path('vehicleedit/<pk>',VehicleUpdateView.as_view(),name='vehicleedit'),
    path('register/',views.register,name="register"),
    path('',views.loginpage,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.custom_logout,name='logout'),
]