from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    product1 = Product(name="Naiki Air Shoes", price=50000, description="Deskripsi produk A", image='https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/naiki.jpeg')
    product2 = Product(name="Convoso 50s Shoes", price=40000, description="Deskripsi produk B", image='https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/convose.jpg')
    product3 = Product(name="Adudu Track Jacket", price=22000, description="Deskripsi produk C", image='https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/adudu.jpg')

    products = [product1, product2, product3]
    
    context = {
        'apps_name' : 'Zalohra',
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F',
        'products': products
    }

    return render(request, "main.html", context)