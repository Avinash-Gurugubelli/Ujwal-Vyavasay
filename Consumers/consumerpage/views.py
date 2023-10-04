from django.shortcuts import render
from django.http import HttpResponse


def consumerfunction(request):
    return render(request,'consumerpage/consumerpage.html')

def buy(request):
    #logic
    return render(request,'consumerpage/buy.html')