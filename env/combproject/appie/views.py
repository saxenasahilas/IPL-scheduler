from django.shortcuts import render,redirect,reverse
from .match import Match
from .models import schedule
# Create your views here.


def seeschedule(request):
    e = schedule.objects.all()
    e.delete()
    return render(request, 'schedule.html')

def createschedule(request):
    ddmmyy=request.POST['yymmdd']
    yy=int(ddmmyy[:4])
    mm=int(ddmmyy[5:7])
    dd=int(ddmmyy[8:])
    Match(yy,mm,dd)
    sc=schedule.objects.all()
    return render(request,'scheduled.html',{'sc':sc})
