from django import forms
from django.contrib.auth.models import User
from poll.models import UserProfileInfo,Question,Choice


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')



#class ChoiceForm(forms.ModelForm):
    #class Meta:
        #model = Choice
        #fields = ['first_answer', 'second_answer', 'notes']
