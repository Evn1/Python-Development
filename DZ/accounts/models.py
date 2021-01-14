from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    faculty = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    CATEGORY = (
        ('IT', 'IT'),
        ('Управление', 'Управление'),
        ('Инженерия', 'Инженерия'),
        ('Языки', 'Языки'),
    )
    name = models.CharField(max_length=200, null=True)
    number_of_hours = models.FloatField(null=True)
    schedule = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Registration(models.Model):
    STATUS = (
        ('Начался', 'Начался'),
        ('Не начался', 'Не начался'),
    )
    student = models.ForeignKey(Student, null=True, on_delete = models.SET_NULL)
    course = models.ForeignKey(Courses, null=True,on_delete = models.SET_NULL)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

