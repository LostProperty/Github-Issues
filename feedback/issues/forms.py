from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'body']


class DeveloperIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['status', 'title', 'developer_title', 'body',
            'developer_body']
