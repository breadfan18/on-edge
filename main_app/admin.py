from django.contrib import admin

# Register your models here.

from .models import Classroom, Assignment, Student, Photo

admin.site.register(Classroom)
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(Photo)
