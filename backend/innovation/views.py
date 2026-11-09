
from rest_framework import generics

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Innovation
from .serializers import InnovationSerializer
from .forms import InnovationForm
from accounts.permissions import IsInnovatorOrPolicymaker


# Existing API Views

class InnovationListCreateView(generics.ListCreateAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    permission_classes = [IsInnovatorOrPolicymaker]


class InnovationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    permission_classes = [IsInnovatorOrPolicymaker]


# Webpage Permission Helpers

def can_manage_innovation(user):
    return (
        user.is_superuser
        or user.groups.filter(name='Innovator').exists()
    )


def can_view_innovation(user):
    return (
        can_manage_innovation(user)
        or user.groups.filter(name='Policymaker').exists()
    )


# Innovation List Page

@login_required
def innovation_page(request):
    if not can_view_innovation(request.user):
        return render(request, '403.html', status=403)

    innovations = Innovation.objects.all()

    return render(request, 'innovation/list.html', {
        'innovations': innovations,
        'can_manage': can_manage_innovation(request.user),
    })


# Add Innovation

@login_required
def add_innovation(request):
    if not can_manage_innovation(request.user):
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = InnovationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Innovation added successfully.')
            return redirect('innovation-page')
    else:
        form = InnovationForm()

    return render(request, 'innovation/form.html', {
        'form': form,
        'page_title': 'Add Innovation',
    })


# Edit Innovation

@login_required
def edit_innovation(request, pk):
    if not can_manage_innovation(request.user):
        return render(request, '403.html', status=403)

    innovation = get_object_or_404(Innovation, pk=pk)

    if request.method == 'POST':
        form = InnovationForm(request.POST, instance=innovation)

        if form.is_valid():
            form.save()
            messages.success(request, 'Innovation updated successfully.')
            return redirect('innovation-page')
    else:
        form = InnovationForm(instance=innovation)

    return render(request, 'innovation/form.html', {
        'form': form,
        'page_title': 'Edit Innovation',
    })


# Delete Innovation

@login_required
def delete_innovation(request, pk):
    if not can_manage_innovation(request.user):
        return render(request, '403.html', status=403)

    innovation = get_object_or_404(Innovation, pk=pk)

    if request.method == 'POST':
        innovation.delete()
        messages.success(request, 'Innovation deleted successfully.')

    return redirect('innovation-page')
