import os

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse

from .forms import IssueForm, IssueStatusForm
from .models import Issue, Status
from .models import get_next_or_prev


@login_required
def list_issues(request):
    status_ids = request.GET.getlist('status', False)
    # TODO: validate the ids
    if status_ids:
        issue_list = Issue.objects.filter(status__in=status_ids)
    else:
        issue_list = Issue.objects.all()
    status_form = IssueStatusForm(request.GET)

    # pagination
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)

    return TemplateResponse(request, 'issues/list_issues.html',
        {'issues': issues, 'status_form': status_form})


# TODO: move to utils files
def is_image_file(file_name):
    """
    Simplistic check to see if file is an image
    """
    if not file_name:
        return False
    image_extensions = [
        u'jpg',
        u'jpeg',
        u'png',
        u'gif',
    ]
    extension = os.path.splitext(file_name)[1]
    extension = extension.lower()[1:]
    return extension in image_extensions


@login_required
def issue_details(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issues = Issue.objects.all()
    next = get_next_or_prev(issues, issue, 'next')
    previous = get_next_or_prev(issues, issue, 'prev')
    attached_image = is_image_file(issue.attachment.name)

    if request.method == 'POST':
        # TODO: check user is allowed to set issue to status given (and status is valid)
        status = request.POST.get('status')
        issue.status_id = status
        issue.save()
        # TODO: load up next issue? User test this
    return TemplateResponse(request, 'issues/issue_details.html',
        {'issue': issue,
        'next': next,
        'previous': previous,
        'attached_image': attached_image})


@login_required
def add_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.status = Status.objects.get(name='New')
            issue.reported_by = request.user
            issue.save()
            messages.success(request, 'Issue successfully created',
                fail_silently=True) # for py.test
            return redirect('list_issues')
    else:
        form = IssueForm()
    return TemplateResponse(request, 'issues/add_issue.html', {'form': form})


@login_required
def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save()
            messages.success(request, 'Issue successfully updated',
                fail_silently=True) # for py.test
            return redirect('list_issues')
    else:
        form = IssueForm(instance=issue)
    return TemplateResponse(request, 'issues/edit_issue.html',
        {'form': form, 'issue': issue})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
