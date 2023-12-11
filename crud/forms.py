from django import forms
from django.utils import timezone
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'start_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'startdateid'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'enddateid'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'statusid'}),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')

        if start_date and start_date < timezone.now().date():
            raise forms.ValidationError(
                'Start date cannot be in the past.'
            )

        return start_date

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError(
                'End date must be after the start date.')

        return end_date
