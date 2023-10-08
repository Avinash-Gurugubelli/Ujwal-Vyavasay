from django.shortcuts import render
from django.http import HttpResponse


def farmerfunction(request):
    return render(request,'farmerpage/farmerpage.html')