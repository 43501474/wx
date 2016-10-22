from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def wx(req):
    '''微信接入验证'''
    return HttpResponse(req.GET("echostr",  ""), content_type="text/plain")
