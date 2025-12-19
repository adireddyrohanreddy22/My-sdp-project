from django.contrib import admin
from .models import Student, Course, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('enrollment_number', 'first_name', 'last_name')
	search_fields = ('first_name', 'last_name', 'enrollment_number')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'code')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('student', 'date', 'present')
	list_filter = ('date', 'present')
	search_fields = ('student__first_name', 'student__last_name', 'student__enrollment_number')
