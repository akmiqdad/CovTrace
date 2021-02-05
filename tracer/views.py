from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Tracing
from .forms import StudentForm,TracingForm
from django.contrib.auth import authenticate, login

def ViewHome(request):
   
    return render(request,'index.html')

     
def ViewTracingForm(request):
    if request.method == 'POST':
        form = TracingForm(request.user.username,request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = TracingForm(request.user.username)
    
    context = {}
    context['form'] = form
    # print(form)
    return render(request,'update.html',context)

    

def ViewReport(request):
    Students = Student.objects.all()
    Traces=Tracing.objects.all()
    context = {}
    context['Students'] = Students
    context['Traces'] = Traces
    return render(request,'report.html',context)

def Register(request):
    if request.method == 'POST':
        form = StudentForm(request.user.username,request.POST)
        if form.is_valid():
            form.save()
            return redirect('report')
    else:
        form = StudentForm(request.user.username)

    context = {}
    context['form'] = form
    return render(request,'register.html', context)

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('register')
    else:
        form = UserCreationForm()
    
    context = {}
    context['form'] = form
    return render(request, 'registration/signup.html', context)
