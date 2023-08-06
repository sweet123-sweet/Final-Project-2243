from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm, StudentForm
from django.contrib.auth import authenticate, login
from .models import Student
# Create your views here.
def index(request):
    context={'title':'home'}
    return render(request,'myApp/index.html',context)

def list(request):
    students = Student.objects.order_by('-id') 
    context = {'students' : students, 'title' : 'List'}
    return render(request, "myApp/list.html", context)

def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,("Data Save Successful"))
        #messages.warning(request,("Data Save Successful"))
        #messages.error(request,("Data Save Successful"))
    else:
        form= StudentForm()
    
    context={'form':form, 'title':'create'}
    return render(request,'myApp/create.html',context)

def details(request,idn):
    student= Student.objects.get(pk=idn)
    # form = StudentForm(request.Post or None, instance= student)
    return render(request,"myApp/details1.html",{'student':student, 'title':'Details'})

def edit_student(request,id):
    if request.method == "POST":
        student= Student.objects.get(pk=id)
        form = StudentForm(request.POST or None, instance= student)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST or None, instance= student)
        
    context = {'title':'edit','form': form}
    return render(request,"myApp/edit.html",context)


def register(request):
    msg = None 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            mdg = 'user created'
            return redirect('home')
        else:
            msg = SignUpForm()
    else:
        form = SignUpForm()
    
    context={'form': form, 'msg': msg}
    return render(request,'register.html', context)
