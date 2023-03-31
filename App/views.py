from django.shortcuts import render,redirect
from App.models import VehicleModel
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from .forms import VehicleForm,NewUserForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


class VehicleCreate(CreateView):
    model = VehicleModel
    form_class = VehicleForm
    template_name = 'addvehicle.html'
    success_url = reverse_lazy('addvehicle')
    
    
def Vehiclelist(request):
    vlist = VehicleModel.objects.all()
    return render(request,'vehiclelist.html',{'vlist':vlist})

def Vehicledelete(request,id):
    vehicle = VehicleModel.objects.get(id=id)
    vehicle.delete()
    return redirect('/vehiclelist')

class VehicleUpdateView(UpdateView):
    model = VehicleModel
    form_class = VehicleForm
    template_name = 'addvehicle.html'
    success_url = reverse_lazy('vehiclelist') 
    
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	form = NewUserForm()
	return render (request,'register.html',{'form':form})

def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/home')  
		else:
			return redirect('/')
	
	return render(request, 'login.html')

@login_required
def home(request):
    return render(request,'home.html')


@login_required
def custom_logout(request):
    logout(request)
    return redirect("/")