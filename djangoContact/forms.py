from django import forms
from .models import  Contact
class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', "message"]
    # name=forms.CharField(label="Your name", max_length=50)
    # Email=forms.EmailField(label="Your email", max_length=50)
    # Message=forms.CharField(label="Message")
