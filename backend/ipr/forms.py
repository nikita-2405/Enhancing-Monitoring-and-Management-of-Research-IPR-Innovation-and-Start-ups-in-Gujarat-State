
from django import forms
from .models import IPR


class IPRForm(forms.ModelForm):

    class Meta:
        model = IPR
        fields = [
            'title',
            'applicant_name',
            'institution',
            'ipr_type',
            'description',
            'application_number',
            'status',
            'filing_date',
        ]

        widgets = {
            'filing_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
