"""
URL configuration for mca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="shop index "),
    path('AboutUs/',views.aboutus , name="aboutus"),
    path('Contact/',views.contact, name="Contact "),
    path('trackerignstatus/', views.tracker, name="trackerignstatus"),
    path('search/',views.search, name="search"),
    path('products/<int:myid>',views.productView, name="productView"),
    path('checkout/',views.checkout, name="checkout")
]
