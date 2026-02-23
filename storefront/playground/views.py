from django.shortcuts import render 

# Create your views here.
def hello(request):
    details = {
        'first_name': 'Umesh',
        'last_name': 'Badsara',
    }
    return render(request, 'hello.html', {'details': details})
