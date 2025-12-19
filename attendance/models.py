from django.db import models


class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, blank=True)
	enrollment_number = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name


class Course(models.Model):
	name = models.CharField(max_length=150)
	code = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name


class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.DateField()
	present = models.BooleanField(default=True)

	class Meta:
		unique_together = (('student', 'date'),)

	def __str__(self):
		return f"{self.student} - {self.date} - {'Present' if self.present else 'Absent'}"
