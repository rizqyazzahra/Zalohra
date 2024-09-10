from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    # product1 = Product.object # create object prod
    # product = Product.objects.all()

    product1 = {
        'name': 'Naiki Air Shoes',
        'description': 'Deskripsi Produk A',
        'price': 50000,
        'image_url': 'https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/naiki.jpeg'
    }

    product2 = {
        'name': 'Convoso 50sShoes',
        'description': 'Deskripsi Produk B',
        'price': 40000,
        'image_url': 'https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/convose.jpg'
    }

    product3 = {
        'name': 'Adudu Track Jacket',
        'description': 'Deskripsi Produk C',
        'price': 22000,
        'image_url': 'https://github.com/rizqyazzahra/Zalohra/blob/main/main/templates/images/adudu.jpg'
    }

    products = [product1, product2, product3]
    
    context = {
        'apps_name' : 'Zalohra',
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F',
        'products': products
    }

    return render(request, "main.html", context)