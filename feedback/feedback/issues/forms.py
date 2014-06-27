from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'body']


class IssueStatusForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['status']
