from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def subscription(request):
    return render(request, 'subscription.html')