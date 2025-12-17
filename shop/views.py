from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.
# def index(request):
#     product= Products.objects.all()
#     n=len(product)
#     nslides=n//4+ceil((n/4)-(n//4))
#     param={'no_of_slides':nslides,'product':product,'range':range(1,nslides)} 
# #     return render(request, 'shop/index.html',param) 
# def index(request):
#     product = Products.objects.all()
#     n = len(product)

#     nslides = n // 4 + ceil((n / 4) - (n // 4))

#     params = {
#         'no_of_slides': nslides,
#         'product': product,
#         'range': range(1, nslides)
#     }
#     return render(request, 'shop/index.html', params)
def index(request):
    products = Products.objects.all()

    slides = []
    for i in range(0, len(products), 4):
        slides.append(products[i:i+4])

    return render(request, "shop/index.html", {"slides": slides})


def aboutus(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("we are on contact")
def tracker(request):
    return HttpResponse("we are on tracker")
def search(request):
    return HttpResponse("we are on search")
def productView(request):
    return HttpResponse("we are on productView")
def checkout(request):
    return HttpResponse("we are on checkout")