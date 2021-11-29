from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    return HttpResponse('hello this is testing')
def fnsample(req):
    return render(req,'sample.html')
