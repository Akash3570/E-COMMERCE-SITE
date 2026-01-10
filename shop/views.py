from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Contact
from django.shortcuts import render, redirect
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
    if request.method =="POST":
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        phone=request.POST.get('phone',"")
        message=request.POST.get('message',"")
        Contact.objects.create(
                        name=name,
                        email=email,
                        phone=phone,
                        message=message)
        return redirect('/shop/Contact/')
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