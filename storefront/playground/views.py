from django.shortcuts import render 
from django.db.models import Count
from store.models import Order ,Customer



# Create your views here.
def hello(request):
    details = {
        'first_name': 'Umesh',
        'last_name': 'Badsara',
    }
    queryset = Customer.objects.annotate(
        orders_count = Count('order')
    )
    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'details': details ,'queryset': queryset})
 