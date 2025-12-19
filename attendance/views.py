from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import Student, Attendance
from .forms import StudentForm



def home(request):
	"""Simple homepage for attendance management site."""
	context = {
		'title': 'Attendance Management',
		'message': 'Welcome to the Attendance Management site. This is a starting page.'
	}
	return render(request, 'home.html', context)


def student_list(request):
	students = Student.objects.all().order_by('enrollment_number')
	return render(request, 'attendance/student_list.html', {'students': students})


def create_student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('attendance:student_list')
	else:
		form = StudentForm()
	return render(request, 'attendance/student_form.html', {'form': form, 'form_title': 'Add Student'})


def edit_student(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('attendance:student_list')
	else:
		form = StudentForm(instance=student)
	return render(request, 'attendance/student_form.html', {'form': form, 'form_title': 'Edit Student'})


def delete_student(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == 'POST':
		student.delete()
		return redirect('attendance:student_list')
	return render(request, 'attendance/student_confirm_delete.html', {'student': student})


def mark_attendance(request):
	today = timezone.localdate()
	students = Student.objects.all().order_by('enrollment_number')

	if request.method == 'POST':
		present_ids = request.POST.getlist('present')
		for s in students:
			was_present = str(s.id) in present_ids
			Attendance.objects.update_or_create(student=s, date=today, defaults={'present': was_present})
		messages.success(request, 'Attendance saved successfully.')
		return redirect('attendance:attendance_list')

	return render(request, 'attendance/mark_attendance.html', {
		'students': students,
		'date': today
	})


def attendance_list(request):
	# show today's attendance by default
	date = request.GET.get('date')
	if date:
		from django.utils.dateparse import parse_date
		date_obj = parse_date(date)
	else:
		date_obj = timezone.localdate()

	records = Attendance.objects.filter(date=date_obj).select_related('student')
	return render(request, 'attendance/attendance_list.html', {'records': records, 'date': date_obj})
