from django import forms

from .models import Issue


class bootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(bootStrapModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class IssueForm(bootStrapModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'priority', 'body']


class IssueStatusForm(bootStrapModelForm):
    """
    Used for filtering issues on the list issues page
    """
    class Meta:
        model = Issue
        fields = ['status']
