
from django import forms
from .models import ResearchProject


class ResearchProjectForm(forms.ModelForm):

    class Meta:
        model = ResearchProject
        fields = [
            'title',
            'researcher_name',
            'institution',
            'research_area',
            'description',
            'status',
            'start_date',
            'end_date',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
