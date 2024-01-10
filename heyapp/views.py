from django.shortcuts import render
from django.http import HttpResponse
from . models import Place


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"skating.html",{'result':obj})

#def about(request):
    #return render(request,"about.html")
