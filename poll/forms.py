from django import forms
from django.contrib.auth.models import User
from poll.models import UserProfileInfo,Patient,Choice


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['IDENTITY', 'EDUCCATEGORY', 'EDUCPATIENT', 'SEXPATIENT', 'AGEPATIENT', 'ECUCCARERCAT', 'EDUCCARER', 'SEXCARER', 'AGECARER', 'RELATIONSHIPCARER', 'LIVESIN', 'kentro', 'date', 'NPI', 'STAGE', 'IADL', 'MMSE', 'DOCTOR']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'user', 'patient', 'notes', 'first_answer', 'second_answer']
