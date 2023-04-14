from django import forms
from django.forms import ModelForm
from db_connect.models import *
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput)
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('event_id', 'event_name')




# class User_register_Form(forms.ModelForm):

#     Account_Type_choices = ( 
#     ("1", "Mentor"),
#     ("2", "Tutor"),
#     ("3", "Student")
#     )
#     User_Email = forms.EmailField(label = "Email")
#     Password = forms.CharField(label = "Passcode",max_length = "8")
#     Account_Type = forms.ChoiceField(choices  = Account_Type_choices)
#     class Meta:
#         model = User_register
#         fields = '__all__'