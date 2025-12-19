from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.create_student, name='student_add'),
    path('students/<int:pk>/edit/', views.edit_student, name='student_edit'),
    path('students/<int:pk>/delete/', views.delete_student, name='student_delete'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('records/', views.attendance_list, name='attendance_list'),
]
