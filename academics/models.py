from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True)
    batch_year = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.roll_no} - {self.user.get_full_name() or self.user.username}"


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=120)
    credits = models.PositiveSmallIntegerField(default=3)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True)
    instructor = models.ForeignKey(Faculty, on_delete=models.SET_NULL,
                                   null=True, related_name="courses")
    
    def __str__(self):
        return f"{self.code} - {self.title}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("student", "course")
    
    def __str__(self):
        return f"{self.student} -> {self.course}"


class Grade(models.Model):
    GRADE_CHOICES = [(g, g) for g in ["A+", "A", "B+", "B", "C+", "C", "D", "F"]]
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE,
                                      related_name="grade")
    value = models.CharField(max_length=2, choices=GRADE_CHOICES)
    graded_by = models.ForeignKey(Faculty, on_delete=models.SET_NULL,
                                  null=True)
    graded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.enrollment}: {self.value}"
