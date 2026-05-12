from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    today = datetime.date.today()
    return HttpResponse(f'<h2>Welcome to dashboard!</h2><p>Today: {today}</p>')