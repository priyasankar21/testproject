from django import forms
from .models import *
from django.core import validators
from django.forms import CharField, ModelForm
from django.core.exceptions import ValidationError

class myform(forms.ModelForm):
  
   def clean_titre(self):
        Company_name = self.cleaned_data['Company_name']
        if len(Company_name) > 6:
            raise ValidationError('too long')
        return Company_name
   class Meta:
      model=detail
      fields=["Company_name","Company_address","Landmark","District","State","Pincode","Mobile_number","Email","Machine_name","Machine_condition","Price","Image"]
      
      
form = myform
class myform1(forms.ModelForm):
   class Meta:
      model=buyer

      fields=["Company_name","Person_name","Email","Address","Mobile_number"]
      
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    messages = forms.CharField(widget=forms.Textarea, required=True)