from django.shortcuts import render
from .models import *
from django.utils.translation import gettext as _


def home(request):

    home = User.objects.all()
    return render(request, 'home/home.html', {_('home'): home})


def about(request):
    about = User.objects.all()
    return render(request, 'about/about_us.html', {_('about'): about})


def contant(request):
    contant = User.objects.all()
    return render(request, 'contant/contact.html', {_('contant'): contant})


def menu(request):
    menu = User.objects.all()
    return render(request, 'menu/menu_register.html', {_('menu'): menu})


def recepties(request):
    recepties = User.objects.all()
    return render(request, 'home/recepits-print.html', {_('recepties'): recepties})