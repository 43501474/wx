# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def wx(req):
    '''微信接入验证'''
    return HttpResponse(req.GET.get("echostr",  ""), content_type="text/plain")


def index(req):
    return HttpResponse("Hello, world!")


def echo(req):
    from .reqparser import text_req
    from .rspbuilder.textbuilder import TextMsg
    msg = text_req.parse(req.body)

    if isinstance(msg, text_req.Msg) and msg.MsgType == 'text':
        toUser = msg.FromUserName
        fromUser = msg.ToUserName
        content = "test"
        replyMsg = TextMsg(toUser, fromUser, content)

        return HttpResponse(str(replyMsg), content_type="text/xml")
