from django import forms
from django.urls import reverse_lazy
from .models import Contact, TechsupportAnswer
from django.db import models

class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']



#  Форма проверки заявки для сотрудников
# class RequestReviewForm(forms.ModelForm):
#     contact = forms.ModelChoiceField(queryset=Contact.objects.all())
    
#     class Meta:
#         model = TechsupportAnswer
#         fields = ['answer', 'contact']



class RequestReviewForm(forms.ModelForm):
    contact = forms.ModelChoiceField(queryset=Contact.objects.all(), widget=forms.Select(attrs={'onchange': 'getContactDetails(this.value)'}))


    class Meta:
        model = TechsupportAnswer
        fields = ['answer', 'contact']

    def __init__(self, *args, **kwargs):
        super(RequestReviewForm, self).__init__(*args, **kwargs)
        if self.instance.contact_id:
            self.fields['first_name'].initial = self.instance.contact.first_name
            self.fields['last_name'].initial = self.instance.contact.last_name
            self.fields['email'].initial = self.instance.contact.email
            self.fields['message'].initial = self.instance.contact.message
