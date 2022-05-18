from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReserveForm



def reserve(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foods:food_list')
    else:
        form = ReserveForm()

    context = {
        'form': form,
    }

    return render(request, 'reservation/reservation.html', context)