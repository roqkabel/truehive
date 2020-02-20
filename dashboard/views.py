from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import EditProjectModelForm
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def projects_view(request):
    projects = Project.objects.filter(user=request.user)
    context = {
        'projects': projects
    }
    return render(request, 'dashboard/projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'dashboard/project_detail.html', context)


def projects_create_view(request):

    form = EditProjectModelForm()

    if request.method == 'POST':
        form = EditProjectModelForm(
            request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/dashboard/projects/')
        else:
            form = EditProjectModelForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/project_add.html', context)


def project_edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = EditProjectModelForm(instance=project)

    if request.method == 'POST':
        form = EditProjectModelForm(
            request.POST, request.FILES, instance=project)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else:
            form = EditProjectModelForm(instance=project)

    context = {
        'form': form,
        'project': project
    }
    return render(request, 'dashboard/project_edit.html', context)


def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('/dashboard/projects/')
