from django.shortcuts import render
from projects.models import Project
# Create your views here.

def project_showcase(request):
    projects =Project.object.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_showcase.html', context)

def project_detail(request, pk):
        project = Project.object.get(pk=pk)
        context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


