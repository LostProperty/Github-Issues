from github import Github

from django.shortcuts import redirect
from django.conf import settings
from django.template.response import TemplateResponse

from .github_utils import get_label
from .forms import IssueForm


def list_issues(request):
    # TODO: investigate Oauth2 key/secret http://developer.github.com/v3/#authentication
    github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
    #github = Github(settings.GITHUB_API_TOKEN)
    github_repo = github.get_repo(settings.ISSUES_REPO)
    filter_label = get_label(github_repo, settings.ISSUES_LABEL)
    # TODO: automatically create label if it doesn't exist
    issues = github_repo.get_issues(labels=[filter_label])
    return TemplateResponse(request, 'issues/list_issues.html',
        {'issues': issues})


def add_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
            github_repo = github.get_repo(settings.ISSUES_REPO)
            label = get_label(github_repo, settings.ISSUES_LABEL)
            github_repo.create_issue(form.cleaned_data['title'],
                form.cleaned_data['body'],
                labels=[label])
            # TODO: flash message (and display on table)
            return redirect('list_issues')
    else:
        form = IssueForm()
    return TemplateResponse(request, 'issues/add_issue.html', {'form': form})
