from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm



def reserve(request):
    # form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            reserve = Reservation(name=name, email=email, phone=phone)
            reserve.save()
    # else:
    #     form = ReservationForm()

    context = {
        'reserve': reserve
    }

    return render(request, 'reservation/reservation.html', context)