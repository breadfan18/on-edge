from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Routes for Classrooms
    path('classrooms/', views.classrooms_index, name='classrooms_index'),
    path('classrooms/<int:classroom_id>/', views.classrooms_detail, name='classrooms_detail'),
    path('classrooms/create/', views.ClassroomCreate.as_view(), name='classrooms_create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classrooms_update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classrooms_delete'),
    # Routes for Students
    path('students/', views.students_index, name='students_index'),
    path('students/<int:student_id>/', views.students_detail, name='students_detail'),
    path('students/create/', views.StudentsCreate.as_view(), name='students_create'),
    path('students/<int:pk>/update/', views.StudentsUpdate.as_view(), name='students_update'),
    path('students/<int:pk>/delete/', views.StudentsDelete.as_view(), name='students_delete'),
    path('students/<int:student_id>/add_photo', views.add_photo, name='add_photo'),
    # Routes for Assignments
    path('assignments/', views.assignments_index, name='assignments_index'),
    path('assignments/<int:assignment_id>/', views.assignments_detail, name='assignments_detail'),
    path('assignments/create/', views.AssignmentCreate.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/update', views.AssignmentUpdate.as_view(), name='assignments_update'),
    path('assignments/<int:pk>/delete', views.AssignmentDelete.as_view(), name='assignments_delete'),
    # Routes for User Auth
    path('accounts/signup/', views.signup, name='signup'), 

    # Associate assignments to classroom 
    path('classrooms/<int:classroom_id>/assoc_assignment/<int:assignment_id>/', views.assoc_assignment_to_classroom, name='assoc_assignment'),
    # Unassociate assignments to classroom 
    path('classrooms/<int:classroom_id>/unassoc_assignment/<int:assignment_id>/', views.unassoc_assignment_to_classroom, name='unassoc_assignment'),
    
    path('classrooms/<int:classroom_id>/assoc_student/<int:student_id>/', views.assoc_student_to_classroom, name='assoc_student'),
    path('classrooms/<int:classroom_id>/unassoc_student/<int:student_id>/', views.unassoc_student_to_classroom, name='unassoc_student'),
    
    # Router for Dashboard
    path('dashboard/', views.dashboard, name='dashboard'), 
    
]