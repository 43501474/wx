# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client


class ViewTestCase(TestCase):

    def setUp(self):
        pass

    def test_status_code(self):
        client = Client()
        response = client.get('/m/wx?echostr=xow')
        self.assertEqual(
            response.status_code, 200, "status code should be 200")

    def test_content(self):
        client = Client()
        response = client.get('/m/wx?echostr=xow')
        self.assertEqual(
            response.content, b"xow", "status code should be 200")

    def test_echo(self):
        post_data = '''<xml>
<ToUserName><![CDATA[111111111]]></ToUserName>
<FromUserName><![CDATA[222222222]]></FromUserName>
<CreateTime>1460537339</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[Welcome]]></Content>
<MsgId>6272960105994287618</MsgId>
</xml>'''
        client = Client()
        rsp = client.post('/m/echo', post_data, content_type="text/xml")
        print(str(rsp))
        print(rsp.content)
