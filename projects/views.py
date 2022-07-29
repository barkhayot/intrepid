from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from accounts.models import Account

# Create your views here.

# Get all projects

def GetProjects(request):
    project = Project.objects.all().order_by('created_at')
    
    context = {
        'projects' : project
    }
    return render(request, 'projects/get-all.html', context)

# Get project detail 

def GetProjectDetail(request, pk): 
    project = get_object_or_404(Project, pk=pk)

    context = {
        'project' : project
    }
    return render(request, 'projects/get-detail.html', context)

# Project Create (Clients)

def CreateProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.company = request.user
            data.save()
            return redirect('getprojects')
    context = {
        'form': form
    }
    return render(request, 'projects/create-project.html', context)

# Delete Project 

def DeleteProject(request, pk):
    project = get_object_or_404(Project, company=request.user, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('getprojects')
    context = {
        'project' : project
    }
    return render(request, 'projects/delete-project', context)