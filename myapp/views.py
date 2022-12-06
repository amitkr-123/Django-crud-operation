from django.shortcuts import render ,redirect
from django.http import HttpResponse
from myapp.models import Student
from django.contrib import messages

def index(request):
    student = Student.objects.all()
    return render(request, 'index.html' , {"student" : student})

def add(request):
    if request.method =='POST':
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        Student(name = name , roll = roll , dept = dept ).save()
        messages.success(request , "Student Added Successfully")
        return redirect("home")

def remove(request , id):
    Student.objects.get(id = id).delete()
    messages.success(request , "Student Deleted Successfully")
    return redirect('home')

def edit(request , id):
    student = Student.objects.get(id=id)
    return render(request , 'edit.html' , {"student" : student})


def update(request , id):
  if request.method =='POST':
    student = Student.objects.get(id = id)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.dept = request.POST.get('dept')
    student.save()
    messages.success(request , "Student Details Updated Successfully")
    return redirect('home')