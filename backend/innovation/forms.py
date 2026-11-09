
from django import forms
from .models import Innovation


class InnovationForm(forms.ModelForm):

    class Meta:
        model = Innovation
        fields = [
            'title',
            'innovator_name',
            'institution',
            'innovation_area',
            'description',
            'status',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
