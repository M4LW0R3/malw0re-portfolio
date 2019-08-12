from django.shortcuts import render
from projects.models import Project
# Create your views here.
def project_showcase(request):
    projects =Project.object.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_showcase.html', context)
