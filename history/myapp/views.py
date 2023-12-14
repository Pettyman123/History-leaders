from django.shortcuts import render
from django.http import HttpResponse
from .forms import leaderform
from .import models
# Create your views here.

def ind(request):
    return render(request,'index.html')

#def home(request):
#    return render(request, 'home.html')

def get_name(request):
    if request.method =="POST":
        form = leaderform(request.POST)
        return HttpResponse('HELLOW WORLDH')
    else:
        form = leaderform()
        return render(request, "index.html", {"form":form})
    

def get_data(request):
    data = models.leaders.objects.all()
    return render(request, 'details.html', {'data':data})
