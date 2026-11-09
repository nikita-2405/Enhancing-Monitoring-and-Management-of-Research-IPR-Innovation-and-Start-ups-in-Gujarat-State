from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from research.models import ResearchProject
from innovation.models import Innovation
from ipr.models import IPR
from startup.models import Startup


@login_required
def analytics_home(request):

    context = {
        'research_count': ResearchProject.objects.count(),
        'innovation_count': Innovation.objects.count(),
        'ipr_count': IPR.objects.count(),
        'startup_count': Startup.objects.count(),
    }

    return render(request, 'analytics/home.html', context)