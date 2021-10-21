from django import forms

from myftsapp.models import *
from django.core import validators
from django.core.validators import RegexValidator

# This class is for signup page
class hotel_form(forms.ModelForm):

    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username'}))
    first_name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name'}))
    last_name= forms.CharField(required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Enter your last name'}))
    email = forms.EmailField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=10)                         
    password = forms.CharField(widget = forms.PasswordInput (attrs={'placeholder':'xxxxxxxx'}),validators=[validators.MinLengthValidator (8)])
    re_password = forms.CharField(widget = forms.PasswordInput (attrs={'placeholder':'xxxxxxxx'}))


    class Meta:
        model=SignUp
        fields="__all__"

    def clean(self):
      super(hotel_form, self).clean()

     
      password = self.cleaned_data.get('password')
      re_password = self.cleaned_data.get('re_password')

      # validating the username and password
      
      first_name = self.cleaned_data.get('first_name')
      if not first_name.isalpha():
           raise forms.ValidationError("first_name should be in alphabets")
      
      last_name = self.cleaned_data.get('last_name')
      if not last_name.isalpha():
           raise forms.ValidationError("last_name should be in alphabets")
      
      if password != re_password:
         self._errors['re_password'] = self.error_class(['confirm Password does not match'])

      return self.cleaned_data

# #This class is for login page 

class login_form(forms.Form):
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username'})) 

    password = forms.CharField(widget = forms.PasswordInput (attrs={'placeholder':'xxxxxxxx'}),validators=[validators.MinLengthValidator (8)])


