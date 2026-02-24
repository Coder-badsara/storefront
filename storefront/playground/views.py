from django.shortcuts import render 
from store.models import Order



# Create your views here.
def hello(request):
    details = {
        'first_name': 'Umesh',
        'last_name': 'Badsara',
    }
    orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'details': details , 'orders':orders})
