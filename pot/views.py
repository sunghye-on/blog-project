from django.shortcuts import render
from .models import Pot
# Create your views here.
def pot(request):
    
    pp = Pot.objects
    return render(request ,'pot.html',{"pp" : pp})