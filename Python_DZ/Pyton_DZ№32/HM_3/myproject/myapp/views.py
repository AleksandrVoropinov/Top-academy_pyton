from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    current_date = datetime.now()
    return render(request, 'current_datetime.html', {'current_date': current_date})

# Create your views here.
