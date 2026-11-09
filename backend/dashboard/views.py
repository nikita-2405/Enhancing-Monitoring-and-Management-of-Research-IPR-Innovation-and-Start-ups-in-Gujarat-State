
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from research.models import ResearchProject
from innovation.models import Innovation
from ipr.models import IPR
from startup.models import Startup


@login_required
def dashboard_home(request):
    user = request.user

    role = ', '.join(user.groups.values_list('name', flat=True)) or 'User'

    context = {
        'research_count': ResearchProject.objects.count(),
        'innovation_count': Innovation.objects.count(),
        'ipr_count': IPR.objects.count(),
        'startup_count': Startup.objects.count(),

        'username': user.username,
        'is_authenticated': user.is_authenticated,
        'role': role,
        'is_admin': user.is_superuser,
    }

    return render(request, 'dashboard/home.html', context)
