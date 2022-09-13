from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from admin_panel.middlewares.login import *


# Create your views here.

@test_middleware
def index(request):
    return render(request,'admin_panel/index.html')


