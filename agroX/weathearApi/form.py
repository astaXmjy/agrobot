from django import forms
from .models import Contact
class ContactUs(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']