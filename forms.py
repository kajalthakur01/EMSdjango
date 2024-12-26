from django import forms
from EMSapp.models import *

# class contactfrom(forms.Form):
#     name=forms.CharField(label='fullname')
#     email=forms.EmailField(required=False)
#     message=forms.CharField()

class Contactform(forms.ModelForm):

    class meta:
        model =ContactEnquiry
        fields =('name','email','message')