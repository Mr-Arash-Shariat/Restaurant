from django import forms
from .models import Reservation



class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()


    # class Meta:
    #     model = Reservation
    #     fields = "__all__"
        
    #     widgets = {
    #         "name": forms.TextInput(attrs={
    #             "placeholder": "Enter your name"
    #         }),
    #         "email": forms.EmailInput(attrs={
    #             "placeholder": "Enter your email"
    #         }),
    #         "phone": forms.NumberInput(attrs={
    #             "placeholder": "Enter your phonenumber"
    #         })
    #     }

    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         new_data = {
    #             'class': 'form-control'
    #         }
    #         self.fields[str(field)].widget.attrs.update(
    #             new_data
    #         )