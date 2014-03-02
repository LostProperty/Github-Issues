from django import forms


class IssueForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(),
        max_length=500,
        required=True)
        #label='What\'s your favourite...')
    # TODO: add body as well
