from dataclasses import field
from pyexpat import model
from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        # Special widgets
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your title..."
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Please enter the valid email..."
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Enter the message please..."
            })
        }

    # Widget for all
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )