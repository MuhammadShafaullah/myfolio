from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #for creating user
from django.contrib.auth.forms import AuthenticationForm #for Login 
from django.contrib.auth.forms import UsernameField #for Login 
from django.utils.translation import gettext,gettext_lazy as _


#SignUp UserCreationForm Custom form 
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email']
        labels= {'username':'Name','email':'Email',}
        
        widgets={'username':forms.TextInput(attrs={'class':'form-control',}),
                'email':forms.TextInput(attrs={'class':'form-control'})
        }
        
       
class SignInForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=UsernameField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True, 'class':'form-control'})) 
    