from django import forms
from .models import Education, ContactUs


class EductationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["title", "starting_date", "ending_date",
                  "institution_name", "description"]


# class ContactUsForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     message = forms.CharField(
#         widget=forms.Textarea()
#     )

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "subjects", "message"]
        widgets = {
            'name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            'email': forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            'subjects': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            'message': forms.Textarea(
                attrs={"class": "form-control",
                       "placeholder": "Enter Your Message"}
            )
        }
