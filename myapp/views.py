from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requst):
    return HttpResponse('Welcome!')
def selfcommend(requst):
    return HttpResponse("i'm "+id)


def index(requst):
    return HttpRequest('Welcome!')
    
def index(requst):
    return HttpRequest('Welcome!')