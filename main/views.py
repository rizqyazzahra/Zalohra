from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Zalohra',
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)