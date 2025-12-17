from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request): 
    return render(request, 'shop/index.html') 
def aboutus(request):
    # context = {
    #     "company_name": "My Awesome Cart",
    #     "mission": "To make online shopping simple, reliable and fast."
    # }
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