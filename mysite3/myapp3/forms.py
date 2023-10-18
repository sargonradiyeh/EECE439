from django import forms
from .models import ContactList
class CreateContactForm(forms.Form):
     name = forms.CharField(label='Name')
     address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'maxlength': '50'}))
     profession = forms.CharField(label='Profession')
     confirmprofession= forms.CharField(label='Profession Confirmation')
     telnumber = forms.IntegerField(label='Telephone Number')
     email = forms.EmailField(label='Email')
     datejoined= forms.DateTimeField(
        label='Date Joined',
        widget=forms.DateInput(attrs={'type': 'date'}),)
     dateexpired = forms.DateField(
        label='Date Expired',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

class UpdateContactForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = ['name', 'address','profession','confirmprofession','telnumber','email','datejoined','dateexpired']
        
    def __init__(self, *args, **kwargs):
        super(UpdateContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['profession'].widget.attrs.update({'class': 'form-control'})
        self.fields['confirmprofession'].widget.attrs.update({'class': 'form-control'})
        self.fields['telnumber'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['datejoined'].widget.attrs.update({'class': 'form-control'})
        self.fields['dateexpired'].widget.attrs.update({'class': 'form-control'})
        