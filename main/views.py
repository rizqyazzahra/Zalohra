from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'apps_name' : 'Zalohra',
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F',
        'products': products
    }

    return render(request, "main.html", context)