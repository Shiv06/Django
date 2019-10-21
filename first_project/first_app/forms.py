from django import forms
from django.core import validators
# from first_app.models import Register
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo
# Create you own custom validators
#
# def check_for_name(value):
#     if value[0].lower() !='z' : raise forms.ValidationError('Name Needs to start with z')
#
# class Registration(forms.ModelForm):
#     class Meta():
#         model=Register
#         fields='__all__'
#         widget={
#         'password':forms.PasswordInput,
#         'confirm_password':forms.PasswordInput
#         }
#
#

#

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    confirm_email=forms.EmailField()
    class Meta():
        model=User
        fields=('username','email','confirm_email','password','confirm_password')


    def clean(self):
        ## verify the emails
        data=super().clean()
        print(data)
        if data['email'] != data['confirm_email']: raise forms.ValidationError("Email does not match!")
        if data['password'] != data['confirm_password']: raise forms.ValidationError("Password does not match!")
        try:
            db_email=Register.objects.get(email=data['email'])
            if db_email: raise forms.ValidationError("Email Already Exists! Please Try Login")

        except:
            print('This is new Email!')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
