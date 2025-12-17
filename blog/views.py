from django.shortcuts import render

def new_index(request):
    return render(request, 'blog/index.html')  
