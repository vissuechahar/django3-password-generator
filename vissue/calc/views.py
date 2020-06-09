from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'home.html')

def password(request):
    
    character=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list('@#$%^&()_+*'))

    thepass=""
    length=int(request.GET.get('length',3))
    lowercase=request

    for i in range(length):
        thepass+=random.choice(character)

    return render(request,'result.html',{'password':thepass})

def vissue(request):
    return render(request,'base.html')