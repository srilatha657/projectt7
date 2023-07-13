from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
data="""<table><tr><th>Empno</th><th>Ename</th><th>Esal</th></tr><tr><td>7788</td><td>scott</td><td>3000.00</td></tr><tr><td>7902</td><td>blake</td><td>4000.00</td></tr><tr><td>7369</td><td>miller</td><td>3500.00</td></tr></table>"""
class HtmlView(View):
    def get(self,request):
        res=HttpResponse(data,content_type="text/html")
        return res
class XmlView(View):
    def get(self,request):
        res=HttpResponse(data,content_type="application/xml")
        return res
class ExcelView(View):
    def get(self,request):
        res=HttpResponse(data,content_type="application/vnd.ms-excel")
        return res