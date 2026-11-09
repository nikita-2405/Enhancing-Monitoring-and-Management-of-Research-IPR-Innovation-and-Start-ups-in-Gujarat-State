
from django import forms
from .models import Startup


class StartupForm(forms.ModelForm):

    class Meta:
        model = Startup
        fields = [
            'name',
            'founder_name',
            'institution',
            'sector',
            'description',
            'stage',
            'status',
            'founded_date',
        ]

        widgets = {
            'founded_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
