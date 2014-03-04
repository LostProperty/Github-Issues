from django import forms


class IssueForm(forms.Form):
    title = forms.CharField(max_length=500, required=True)
    body = forms.CharField(widget=forms.Textarea(),
        max_length=5000, required=False)
