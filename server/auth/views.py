from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register():
    return HttpResponse("Hello, you are at the register endpoint")
