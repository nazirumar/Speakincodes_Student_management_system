
from dataclasses import field
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import BioUpdate, O_Level, Pincode

Choices=(   
    ( ("1"),'Basic Nursing'),
    (("2"),"Basic MIDWIFERY")

)


gender =(
    (('1'), 'Male'),
    (('2'), 'FeMale'),

)


class BioUpdateForms(forms.ModelForm):
    class Meta:
        model = BioUpdate
        fields="__all__"


class O_LEVEL(forms.ModelForm):
    class Meta:
        model= O_Level
        fields =['Subject','Name_School', 'Examination_type','Examination_No', 'Year','grade']



class PincodeForm(forms.ModelForm):
    class Meta:
        model= Pincode
        fields ='__all__'