from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def wx(req):
    '''微信接入验证'''
    return HttpResponse(req.GET.get("echostr",  ""), content_type="text/plain")


def index(req):
    return HttpResponse("Hello, world!")
