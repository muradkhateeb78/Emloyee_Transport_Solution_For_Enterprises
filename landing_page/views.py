from django.shortcuts import HttpResponse, render
from django.template import loader

# Create your views here.
def index(request):
    # template = loader.get_template('Employee_transport_solution_for_entreprises/home.html')
    # context = {
    #     'Data': ' ',
    # }
    iterations= [1,2,3,4,5,6]
    name = "Murad Khateeb Abbasi"
    context = {
        'loveName':name,
        'numbers': iterations,
    }
    return render(request, 'landing_page/index.html',context)