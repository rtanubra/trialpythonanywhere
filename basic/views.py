from django.shortcuts import render

# Create your views here.
from .models import (
    Owner)

def hello(request):
    return render(request,'basic/hello.html')