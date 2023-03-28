from django.shortcuts import render
from module_1.models import *

# Create your views here.
def index(request):
    list_of_rifles = Rifle.objects.filter()
    
    return render(request, 'module_1/template1.html', {
        'list_of_rifles' : list_of_rifles,
    })    

def create_rifle(request):
    if request.POST.get('btncreaterifle'):
        name = request.POST.get('name')
        place_of_origin = request.POST.get('place_of_origin')
        
        rifle_info = Rifle(name=name,place_of_origin=place_of_origin)
        rifle_info.save()
    
    return render(request, 'module_1/create_rifle.html', {
        
    })
