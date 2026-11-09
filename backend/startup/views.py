
from rest_framework import generics

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Startup
from .serializers import StartupSerializer
from .forms import StartupForm
from accounts.permissions import IsEntrepreneurOrPolicymaker


# Existing API Views

class StartupListCreateView(generics.ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsEntrepreneurOrPolicymaker]


class StartupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsEntrepreneurOrPolicymaker]


# Webpage Permission Helpers

def can_manage_startup(user):
    return (
        user.is_superuser
        or user.groups.filter(name='Entrepreneur').exists()
    )


def can_view_startup(user):
    return (
        can_manage_startup(user)
        or user.groups.filter(name='Policymaker').exists()
    )


# Startup List Page

@login_required
def startup_page(request):
    if not can_view_startup(request.user):
        return render(request, '403.html', status=403)

    startups = Startup.objects.all()

    return render(request, 'startup/list.html', {
        'startups': startups,
        'can_manage': can_manage_startup(request.user),
    })


# Add Startup

@login_required
def add_startup(request):
    if not can_manage_startup(request.user):
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = StartupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Startup added successfully.')
            return redirect('startup-page')
    else:
        form = StartupForm()

    return render(request, 'startup/form.html', {
        'form': form,
        'page_title': 'Add Startup',
    })


# Edit Startup

@login_required
def edit_startup(request, pk):
    if not can_manage_startup(request.user):
        return render(request, '403.html', status=403)

    startup = get_object_or_404(Startup, pk=pk)

    if request.method == 'POST':
        form = StartupForm(request.POST, instance=startup)

        if form.is_valid():
            form.save()
            messages.success(request, 'Startup updated successfully.')
            return redirect('startup-page')
    else:
        form = StartupForm(instance=startup)

    return render(request, 'startup/form.html', {
        'form': form,
        'page_title': 'Edit Startup',
    })


# Delete Startup

@login_required
def delete_startup(request, pk):
    if not can_manage_startup(request.user):
        return render(request, '403.html', status=403)

    startup = get_object_or_404(Startup, pk=pk)

    if request.method == 'POST':
        startup.delete()
        messages.success(request, 'Startup deleted successfully.')

    return redirect('startup-page')
