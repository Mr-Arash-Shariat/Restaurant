from django import forms
from .models import Reservation



class ReserveForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput())
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "form-control"
    # }))

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone')

        # Special widgets
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your title..."
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Please enter the valid email..."
            }),
            "phone": forms.NumberInput(attrs={
                "placeholder": "Enter the phone..."
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