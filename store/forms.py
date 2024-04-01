from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Register(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"floatingInput","placeholder":"name"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"passwordinput","placeholder":"pass"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"passwordinput","placeholder":"pass"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"passwordinput","placeholder":"name"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"passwordinput","placeholder":"name"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"passwordinput","placeholder":"name"}))
    
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
      

class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"floatingInput","placeholder":"name"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"PasswordInput","placeholder":"name"}))

class orderform(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","rows":5}))


                                        
    
   