from django import forms

from .models import Issue, Status


class bootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(bootStrapModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class IssueForm(bootStrapModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'priority', 'body']


class IssueStatusForm(forms.ModelForm):
    """
    Used for filtering issues on the list issues page
    """
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(),
        widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Issue
        fields = ['status']
