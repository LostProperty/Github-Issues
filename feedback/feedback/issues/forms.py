from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'priority', 'body']


class IssueStatusForm(forms.ModelForm):
    """
    Used for filtering issues on the list issues page
    """
    class Meta:
        model = Issue
        fields = ['status']
