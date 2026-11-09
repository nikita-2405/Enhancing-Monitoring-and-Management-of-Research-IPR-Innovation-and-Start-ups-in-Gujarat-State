
from rest_framework import generics

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import IPR
from .serializers import IPRSerializer
from .forms import IPRForm
from accounts.permissions import IsIPRProfessionalOrPolicymaker


# Existing API Views

class IPRListCreateView(generics.ListCreateAPIView):
    queryset = IPR.objects.all()
    serializer_class = IPRSerializer
    permission_classes = [IsIPRProfessionalOrPolicymaker]


class IPRDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPR.objects.all()
    serializer_class = IPRSerializer
    permission_classes = [IsIPRProfessionalOrPolicymaker]


# Webpage Permission Helpers

def can_manage_ipr(user):
    return (
        user.is_superuser
        or user.groups.filter(name='IPR Professional').exists()
    )


def can_view_ipr(user):
    return (
        can_manage_ipr(user)
        or user.groups.filter(name='Policymaker').exists()
    )


# IPR List Page

@login_required
def ipr_page(request):
    if not can_view_ipr(request.user):
        return render(request, '403.html', status=403)

    ipr_records = IPR.objects.all()

    return render(request, 'ipr/list.html', {
        'ipr_records': ipr_records,
        'can_manage': can_manage_ipr(request.user),
    })


# Add IPR Record

@login_required
def add_ipr(request):
    if not can_manage_ipr(request.user):
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = IPRForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'IPR record added successfully.')
            return redirect('ipr-page')
    else:
        form = IPRForm()

    return render(request, 'ipr/form.html', {
        'form': form,
        'page_title': 'Add IPR Record',
    })


# Edit IPR Record

@login_required
def edit_ipr(request, pk):
    if not can_manage_ipr(request.user):
        return render(request, '403.html', status=403)

    ipr_record = get_object_or_404(IPR, pk=pk)

    if request.method == 'POST':
        form = IPRForm(request.POST, instance=ipr_record)

        if form.is_valid():
            form.save()
            messages.success(request, 'IPR record updated successfully.')
            return redirect('ipr-page')
    else:
        form = IPRForm(instance=ipr_record)

    return render(request, 'ipr/form.html', {
        'form': form,
        'page_title': 'Edit IPR Record',
    })


# Delete IPR Record

@login_required
def delete_ipr(request, pk):
    if not can_manage_ipr(request.user):
        return render(request, '403.html', status=403)

    ipr_record = get_object_or_404(IPR, pk=pk)

    if request.method == 'POST':
        ipr_record.delete()
        messages.success(request, 'IPR record deleted successfully.')

    return redirect('ipr-page')
