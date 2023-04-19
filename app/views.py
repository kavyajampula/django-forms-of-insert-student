from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            sid=SFD.cleaned_data['sid']
            sname=SFD.cleaned_data['sname']
            semail=SFD.cleaned_data['semail']
            SO=Student.objects.get_or_create(sid=sid,sname=sname,semail=semail)[0]
            SO.save()
            
            SQS=Student.objects.all()
            d1={'SQS':SQS}
            return render(request,'display_students.html',d1)
    return render(request,'insert_student.html',d)   
