from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is my first function')
def uma(request):
    return HttpResponse('uma is good girl')
