from django.shortcuts import render
from datetime import datetime

def programmer_day(request):
    year = datetime.now().year
    programmer_day_date = datetime(year, 1, 1) + timedelta(days=255)
    return render(request, 'programmer_day.html', {'programmer_day_date': programmer_day_date})
# Create your views here.
