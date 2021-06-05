from django.shortcuts import render, redirect
from .forms import ClaimForm
from .models import *


# Create your views here.


def homepage(request):
    return render(request,
                  'core/homepage.html',
                  context={'homepage': homepage})


def mentors_info(request):
    all_mentors = Mentors.objects.all()
    return render(
        request,
        'core/mentors.html',
        context={'all_mentors': all_mentors}
    )


def details(request, id):
    course_details = Course.objects.get(id=id)
    return render(request,
                  'core/details.html',
                  context={'detail': course_details})


def course_info(request):
    all_course = Course.objects.all()
    return render(
        request,
        'core/course.html',
        context={'all_course': all_course}
    )


def Claim(request):
    add_claim = ClaimForm(request.POST)
    if request.method == 'POST':
        if add_claim.is_valid():
            add_claim.save()
            return redirect('homepage')
    else:
        add_claim = ClaimForm
    return render(
        request,
        'core/claim.html',
        context={'add_claim': add_claim}
    )
