from django.shortcuts import render 
from store.models import Product

# Create your views here.
def hello(request):
    details = {
        'first_name': 'Umesh',
        'last_name': 'Badsara',
    }
    products = Product.objects.filter(title__icontains='coffee')
    return render(request, 'hello.html', {'details': details , 'products':products})
