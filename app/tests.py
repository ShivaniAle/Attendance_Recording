from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Staff, Student, Course, Session_Year

class StaffModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='staff_user', password='password123')
        staff = Staff.objects.create(admin=user, address='Test Address', gender='Female')

    def test_staff_creation(self):
        staff = Staff.objects.get(admin__username='staff_user')
        self.assertEqual(staff.address, 'Test Address')

class StudentModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='student_user', password='password123')
        course = Course.objects.create(name='Test Course')
        session_year = Session_Year.objects.create(session_start='2023', session_end='2024')
        student = Student.objects.create(admin=user, address='Test Address', gender='Male', course_id=course, session_year_id=session_year)

    def test_student_creation(self):
        student = Student.objects.get(admin__username='student_user')
        self.assertEqual(student.address, 'Test Address')
