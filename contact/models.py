from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea,label = "Email Message",required=False)
    