from django.shortcuts import render, redirect
from .forms import ReservationForm



def reserve(request):
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foods:food_list')
    else:
        form = ReservationForm()

    context = {
        'forms': form
    }

    return render(request, 'reservation/reservation.html', context)