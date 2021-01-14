from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import RegFilter
from .forms import RegistrationForm


def home(request):
    registrations = Registration.objects.all()
    students = Student.objects.all()
    total_registrations = registrations.count()
    total_students = students.count()
    active = registrations.filter(status='Начался').count()
    inactive = registrations.filter(status='Не начался').count()
    context = {
        'registrations': registrations,
        'students': students,
        'total_registrations': total_registrations,
        'total_students': total_students,
        'active': active,
        'inactive': inactive
    }
    return render(request, 'accounts/dashboard.html', context)


def courses(request):
    courses = Courses.objects.all()
    return render(request, 'accounts/courses.html', {'courses': courses})


def student(request, pk):
    student = Student.objects.get(id=pk)
    registrations = student.registration_set.all()
    registrations_count = registrations.count()
    myFilter = RegFilter(request.GET, queryset=registrations)
    registrations = myFilter.qs
    context = {
        'student': student,
        'registrations': registrations,
        'registrations_count': registrations_count,
        'myFilter': myFilter
    }
    return render(request, 'accounts/student.html', context)


def Register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/registration_form.html', context)
