from django.shortcuts import render, redirect
from .models import Course


# Create your views here.
def index(request):
    context = {
    "courses" : Course.objects.all()
    # select * from Course
    }
    return render(request, "test_app/index.html", context)

def courses(request):
    Course.objects.create(title=request.POST['title'], description=request.POST['description'])
    #insert into courses (title, description, created_at, updated_at) values (title, description now(), now())
    return redirect('/')

def confirm(request, id):
    context = {
        'Course' : Course.objects.all(),
        'courses': Course.objects.get(id=id),
    }
    return render(request, 'test_app/delete.html', context)

def NO(request):
    return redirect('/')

def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
