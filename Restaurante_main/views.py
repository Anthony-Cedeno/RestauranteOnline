from django.shortcuts import render
from django.http import HttpResponse

from vendor.models import Vendor

def home (request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]#El numero es la cantidad de restaurantes que quieres mostrar

    return render(request,'home.html')