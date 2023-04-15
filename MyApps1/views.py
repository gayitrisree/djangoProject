

from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.

def display(request):
     ss = "<h1>Hello User, hieveryone what about your life stile) & First-App(MyApps1)</h1><hr />";
     return HttpResponse(ss);

