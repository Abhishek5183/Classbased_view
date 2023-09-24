from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt = datetime.datetime.now()
    d = {'data' : 'ToDay IS SaTurDAy', 'c' : 1 , 'dt' : dt}
    return render(request, 'filters.html', d)
