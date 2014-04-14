from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse

from .forms import IssueForm, DeveloperIssueForm
from .models import Issue, Status


@login_required
def list_issues(request):
    issues = Issue.objects.all()
    return TemplateResponse(request, 'issues/list_issues.html',
        {'issues': issues})


@login_required
def issues_details(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    return TemplateResponse(request, 'issues/issue_details.html',
        {'issue': issue})


@login_required
def add_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.status = Status.objects.get(name='New')
            issue.save()
            # TODO: abastract the use of Github here
            # github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
            # github_repo = github.get_repo(settings.ISSUES_REPO)
            # label = get_label(github_repo, settings.ISSUES_LABEL)
            # github_repo.create_issue(form.cleaned_data['title'],
            #     form.cleaned_data['body'],
            #     labels=[label])
            # TODO: link back to issue (once we have an view/edit page)
            messages.success(request, 'Issue successfully created')
            return redirect('list_issues')
    else:
        form = IssueForm()
    return TemplateResponse(request, 'issues/add_issue.html', {'form': form})


# TODO: different form for client
@login_required
def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        form = DeveloperIssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            messages.success(request, 'Issue successfully updated')
            return redirect('list_issues')
    else:
        form = DeveloperIssueForm(instance=issue)
    return TemplateResponse(request, 'issues/edit_issue.html',
        {'form': form, 'issue': issue})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
