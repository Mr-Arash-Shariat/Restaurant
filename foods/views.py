from django.shortcuts import render, redirect
from .models import Food



def food_list(request):
    foods = Food.objects.all()

    context = {
        'foods': foods,
    }

    return render(request, 'foods/list.html', context)


def menu(request):
    menu = Food.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'foods/menu.html', context)


def food_detail(request, pk):
    foods = Food.objects.get(id=pk)

    context = {
        'food': foods,
    }

    return render(request, 'foods/detail.html', context)