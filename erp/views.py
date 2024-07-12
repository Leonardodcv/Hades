from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from erp.models import *
# Create your views here.
def myfirstview(request):
    data ={
        "name": "Leonardo",
        "categorias": Category.objects.all()
    }
    return render(request, "index.html", data)

def mysecondview(request):
    data ={
        "name": "Leonardo",
        "products": Product.objects.all()
    }
    return render(request, "second.html", data)

