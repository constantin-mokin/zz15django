from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    name = request.POST.get('name')
    return HttpResponse('len is {}' .format(len(name)))
