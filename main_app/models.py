from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

# Student model 
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Assignment(models.Model):
    description = models.TextField(max_length=1000)
    due_date = models.DateField()
    # completed_date = models.DateField(null=True) 
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('assignments_detail', kwargs={'pk': self.id})

class Classroom(models.Model):
    course_subject = models.CharField(max_length=100)
    course_number = models.IntegerField()
    course_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=CASCADE)
    assignments = models.ManyToManyField(Assignment)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return f'{self.course_subject} {self.course_number}, {self.course_name}'

    def get_absolute_url(self):
        return reverse('classrooms_detail', kwargs={'pk': self.id})

class Profile(models.Model):
  is_teacher = models.BooleanField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, default=None)
  last_name = models.CharField(max_length=100, default=None)
  email = models.EmailField(default=None)

  class Photo(models.Model):
    url = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for student_id: {self.student_id} @{self.url}"