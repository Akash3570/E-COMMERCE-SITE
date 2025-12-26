from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
def index(request):
    all_categories = Products.objects.values('category').distinct()

    all_products = []

    for cat in all_categories:
        products = Products.objects.filter(category=cat['category'])

        slides = []
        for i in range(0, len(products), 4):
            slides.append(products[i:i+4])

        all_products.append({
            "category": cat['category'],
            "slides": slides
        })

    return render(request, "shop/index.html", {
        "all_products": all_products
    })
def aboutus(request):
    return render(request, "shop/about.html")
def contact(request):
    return render(request, "shop/contact.html")
def tracker(request):
    return render(request, "shop/tracker.html")
def search(request):
    return render(request, "shop/search.html")
def productView(request,myid):
   products = Products.objects.get(id =myid)
   return render(request, "shop/prodview.html",{'products':products})
def checkout(request):
   return render(request, "shop/checkout.html")