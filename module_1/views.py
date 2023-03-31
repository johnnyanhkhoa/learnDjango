from django.shortcuts import render
from django.contrib import messages
from module_1.models import *
from module_1.forms import * 

# Create your views here.
def index(request):
    list_of_rifles = Rifle.objects.filter()
    
    return render(request, 'module_1/template1.html', {
        'list_of_rifles' : list_of_rifles,
    })    

def create_rifle(request):
    frm_create_rifle = FormCreateRifle()
    if request.POST.get('btncreaterifle'):
        frm_create_rifle = FormCreateRifle(request.POST, Rifle)
        if frm_create_rifle.is_valid():
            post = frm_create_rifle.save(commit=False)
            post.name = frm_create_rifle.cleaned_data['name']
            post.place_of_origin = frm_create_rifle.cleaned_data['place_of_origin']
            post.save()
            messages.success(request, 'Data created !')
        else:
            messages.error(request, 'Not valid !')
    
    return render(request, 'module_1/create_rifle.html', {
        'frm_create_rifle' : frm_create_rifle,
    })
