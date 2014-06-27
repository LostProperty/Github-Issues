from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse

from .forms import IssueForm, IssueStatusForm
from .models import Issue, Status


@login_required
def list_issues(request):
    status_id = request.GET.get('status', False)
    if status_id: # TODO: check is int and is_integer(status_id):
        status = get_object_or_404(Status, pk=status_id)
        issues = Issue.objects.filter(status=status)
    else:
        issues = Issue.objects.all()
    status_form = IssueStatusForm(request.GET)

    return TemplateResponse(request, 'issues/list_issues.html',
        {'issues': issues, 'status_form': status_form})


@login_required
def issues_details(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        # TODO: check user is allowed to set issue to status given (and status is valid)
        status = request.POST.get('status')
        issue.status_id = status
        issue.save()
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
            messages.success(request, 'Issue successfully created')
            return redirect('list_issues')
    else:
        form = IssueForm()
    return TemplateResponse(request, 'issues/add_issue.html', {'form': form})


@login_required
def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            messages.success(request, 'Issue successfully updated')
            return redirect('list_issues')
    else:
        form = IssueForm(instance=issue)
    return TemplateResponse(request, 'issues/edit_issue.html',
        {'form': form, 'issue': issue})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
