from django.shortcuts import HttpResponse, render
from django.template import loader

# Create your views here.
def index(request):
    name = 'murad'
    context = {
        'yourName': name,
    }
    return render(request, 'transport_resources/index.html',context)