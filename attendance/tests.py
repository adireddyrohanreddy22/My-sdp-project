from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from .models import Student, Attendance


class AttendanceViewTests(TestCase):
	def setUp(self):
		self.s = Student.objects.create(first_name='T', last_name='User', enrollment_number='ENR999')
		# create and authenticate a test user because views require login
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.client.force_login(self.user)

	def test_mark_attendance_saves_and_sets_message(self):
		resp = self.client.post(reverse('attendance:mark_attendance'), {'present': [str(self.s.id)]}, follow=True)
		self.assertRedirects(resp, reverse('attendance:attendance_list'))
		today = timezone.localdate()
		self.assertTrue(Attendance.objects.filter(student=self.s, date=today, present=True).exists())
		messages = list(get_messages(resp.wsgi_request))
		self.assertTrue(any('Attendance saved' in str(m) for m in messages))
