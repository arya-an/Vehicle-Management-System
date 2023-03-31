from django import forms
from .models import VehicleModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class VehicleForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['vehicle_number','vehicle_type','vehicle_model','vehicle_description']
       
class NewUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email','username','password1','password2','is_staff']

        
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field_name in ('email','username','password1','password2','is_staff'):
            self.fields[field_name].help_text = ''