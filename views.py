from django.shortcuts import render,redirect
from django.http import HttpResponse
from EMSapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request,num):
    return HttpResponse(num)

def index(request):
    data={
        'info':[{'name':'abc','age':21},
                {'name':'xyz','age':20},
                {'name':'def','age':19}],

        'products':['fryfruits','spices','rice']           
    }
    return render(request,'index.html',data)
@login_required
def getData(request):
    employee=Employee.objects.all()
    return render (request,'index.html', context={'emp':employee})

def department(request):
    employee=employee.objects.all()
    hod=Department.objects.all()
    return render(request,'index.html',context={'d':index})
   
def about(request):
    return render(request,'about.html')

def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        department=request.POST['department']
        salary=request.POST['salary']
        age=request.POST['age']
        Employee.objects.create(name=name,department=department,salary=salary,age=age)
        return redirect('getData')
    return render(request, 'add-data.html')

def updateData(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
       employee.name=request.POST['name']
       employee.department=request.POST['department']
       employee.salary=request.POST['salary']
       employee.age=request.POST['age']
       employee.save()
       return redirect('getData')
    
    return render(request , 'update.html',context={'emp':employee})




# ---------------------------------Student----------------------------------
def fetch(request):
    student=Student.objects.all()
    return render (request,'stu_data.html', context={'stu':student})

def addStudent(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        rollno=request.POST['rollno']
        age=request.POST['age']
        Student.objects.create(name=name,course=course,rollno=rollno,age=age)
        return redirect('fetch')
    return render(request, 'addstu.html')


def update(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
       student.name=request.POST['name']
       student.course=request.POST['course']
       student.rollno=request.POST['rollno']
       student.age=request.POST['age']
       student.save()
       return redirect('fetch')
    
    return render(request , 'update_stu.html',context={'stu':student})


def deletestu(request,id):
    Student=Student.objects.get(id=id)
    Student.delete()
    return redirect('fetch')





# def sdeleteData(request,id):
#     student=Student.objects.get(id=id)
#     student.delete()
#     return redirect("studentData")


#---------------------------------form------------------------

# def contact(request):
#     form=Contactform()
#     return render(request,'contact.html',context={'f':form})
@login_required
def contactview(request):
    cform =Contactform()
    if request.method=='post':
        cform=Contactform(request.POST)
        cform.save()
        return redirect('contact')
    return render(request,'contact.html', {'f':cform})  

#----------------user register---------------------
def register(request):
    rform=UserCreationForm()
    if request.method=='POST':
        rform=UserCreationForm(request.POST)
        if rform.is_valid():
            rform.save()
            return redirect ('getData')
    return render(request,'userregistration.html',{'f':rform})  




def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('getData')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')















