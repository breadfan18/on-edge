from django.shortcuts import render, redirect
from .models import Classroom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def classrooms_index(req):
    classrooms = Classroom.objects.all()
    return render(req, 'classrooms/index.html', {'classrooms': classrooms})

def classrooms_detail(req, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    return render(req, 'classrooms/detail.html', {'classroom': classroom})
    
class ClassroomCreate(CreateView):
    model = Classroom
    fields = '__all__'
    success_url = '/classrooms/'

class ClassroomUpdate(UpdateView):
    model = Classroom

class ClassroomDelete(DeleteView):
    model = Classroom