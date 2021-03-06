from django.shortcuts import render
from .models import Project


def home(request):
    """
    Default landing home page
    :param request:
    :return:
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
