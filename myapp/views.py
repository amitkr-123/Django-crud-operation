from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student

def index(request):
    student = Student.objects.all()
    return render(request, 'index.html' , {"student" : student})

def add(request):
    if request.method =='POST':
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        Student(name = name , roll = roll , dept = dept ).save()
        return HttpResponse("Student Added Succesfully <a href = '/'> -> Go back <a/> ")

def remove(request , id):
    Student.objects.get(id = id).delete()
    return HttpResponse("Deleted Succesfully <a href = '/'> -> Go back <a/>")

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
    return HttpResponse("Student Updated Succesfully <a href = '/'> -> Go back <a/> ")