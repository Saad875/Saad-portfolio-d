from django.shortcuts import render, HttpResponse
from .models import Education, Skill, Experience, Project

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    return HttpResponse("this is about page")


def my_view(request):
    context = {
        'variable': 'Dynamic Content'
    }
    return render(request, 'index.html', context)


# def index(request):
#     educations = Education.objects.all()
#     skills = Skill.objects.all()
#     experiences = Experience.objects.all()
#     projects = Project.objects.all()
#     return render(request, 'index.html', {
#         'educations': educations,
#         'skills': skills,
#         'experiences': experiences,
#         'projects': projects,
#     })
