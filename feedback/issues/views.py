from github import Github

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from .utils import get_label, get_issue, get_issues
from .forms import IssueForm


@login_required
def list_issues(request):
    filter_label = get_label()
    issues = get_issues(filter_label)
    return TemplateResponse(request, 'issues/list_issues.html',
        {'issues': issues})


@login_required
def issues_details(request, issue_id):
    issue = get_issue(issue_id)
    return TemplateResponse(request, 'issues/issue_details.html',
        {'issue': issue})


@login_required
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
            # TODO: link back to issue (once we have an view/edit page)
            messages.success(request, 'Issue successfully created')
            return redirect('list_issues')
    else:
        form = IssueForm()
    return TemplateResponse(request, 'issues/add_issue.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
