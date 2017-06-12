from django.shortcuts import render

# Create your views here.

def return_404_page(request, *args, **kwargs):
    return render(request, '404page.html')
