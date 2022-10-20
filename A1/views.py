from django.shortcuts import render
import requests
import datetime
from A1.models import *

def home(request):
    return render(request, 'base.html')
