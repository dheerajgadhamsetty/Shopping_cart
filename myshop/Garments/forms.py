from django import forms
# create own forms
class ContactForm(forms.Form):
    contact_name = forms.CharField(label="Enter your name", required=True)
    contact_email = forms.EmailField(label="Enter your email", required=True)
    content = forms.CharField(label="your MSG", required=True, widget=forms.Textarea)
    

