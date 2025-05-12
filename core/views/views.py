# core/views.py
from django.shortcuts import render, redirect
from ..models import Request
from core.forms.request import RequestForm
from core.forms.offer import OfferForm
from ..models import Offer


def request_create_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request-list')
    else:
        form = RequestForm()
    return render(request, 'core/request_form.html', {'form': form})

def request_list_view(request):
    requests = Request.objects.all().order_by('-created_at')
    return render(request, 'core/request_list.html', {'requests': requests})

def offer_create_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offer-list')
    else:
        form = OfferForm()
    return render(request, 'core/offer_form.html', {'form': form})

def offer_list_view(request):
    offers = Offer.objects.all().order_by('-created_at')
    return render(request, 'core/offer_list.html', {'offers': offers})


def request_list_view(request):
    requests = Request.objects.all().order_by('-created_at')
    return render(request, 'core/request_list.html', {'requests': requests})

def request_create_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request-list')
    else:
        form = RequestForm()
    return render(request, 'core/request_form.html', {'form': form})

def offer_list_view(request):
    offers = Offer.objects.all().order_by('-created_at')
    return render(request, 'core/offer_list.html', {'offers': offers})

def offer_create_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offer-list')
    else:
        form = OfferForm()
    return render(request, 'core/offer_form.html', {'form': form})

