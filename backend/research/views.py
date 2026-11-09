
from rest_framework import generics

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ResearchProject
from .serializers import ResearchProjectSerializer
from .forms import ResearchProjectForm
from accounts.permissions import IsResearcherOrPolicymaker


# Existing API Views

class ResearchProjectListCreateView(generics.ListCreateAPIView):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer
    permission_classes = [IsResearcherOrPolicymaker]


class ResearchProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer
    permission_classes = [IsResearcherOrPolicymaker]


# Webpage permission helper

def can_manage_research(user):
    return (
        user.is_superuser
        or user.groups.filter(name='Researcher').exists()
    )


def can_view_research(user):
    return (
        can_manage_research(user)
        or user.groups.filter(name='Policymaker').exists()
    )


# Research Projects List

@login_required
def research_page(request):
    if not can_view_research(request.user):
        return render(request, '403.html', status=403)

    projects = ResearchProject.objects.all()
    return render(request, 'research/list.html', {
        'projects': projects,
        'can_manage': can_manage_research(request.user),
    })


# Add Research Project

@login_required
def add_research(request):
    if not can_manage_research(request.user):
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = ResearchProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Research project added successfully.')
            return redirect('research-page')
    else:
        form = ResearchProjectForm()

    return render(request, 'research/form.html', {
        'form': form,
        'page_title': 'Add Research Project',
    })


# Edit Research Project

@login_required
def edit_research(request, pk):
    if not can_manage_research(request.user):
        return render(request, '403.html', status=403)

    project = get_object_or_404(ResearchProject, pk=pk)

    if request.method == 'POST':
        form = ResearchProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Research project updated successfully.')
            return redirect('research-page')
    else:
        form = ResearchProjectForm(instance=project)

    return render(request, 'research/form.html', {
        'form': form,
        'page_title': 'Edit Research Project',
    })


# Delete Research Project

@login_required
def delete_research(request, pk):
    if not can_manage_research(request.user):
        return render(request, '403.html', status=403)

    project = get_object_or_404(ResearchProject, pk=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Research project deleted successfully.')

    return redirect('research-page')
