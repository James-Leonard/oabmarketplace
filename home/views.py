from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignupForm


def frontpage(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'items': items,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    return render(request, 'home/contact.html')


def signup1(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'home/signup.html', {
        'form': form
    })
