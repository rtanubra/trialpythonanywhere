from django.shortcuts import render

# Create your views here.
from .models import (
    Owner
)

def hello(request):
    owners = Owner.objects.all()
    return render(request,'basic/hello.html',{'owners':owners})