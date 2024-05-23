from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Name
# Create your views here.
def hello(request):
    return render(request,'index.html')

def greet(request):
    # names =[
    #     'Sophia Davies',
    #     'Jake Daniels',
    #     'Omotola Hakainde',
    #     'Aubrey Duckworth',
    #     'Jermaine Graham'
    # ]
    # index = random.randint(1,5)
    # name = names[index]
    names = Name.objects.all()
    name = random.choice(names)
    return render(request,'greet.html',{'name':name})