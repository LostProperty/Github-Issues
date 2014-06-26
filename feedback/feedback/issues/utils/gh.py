# Note can't call this file github.py as that causes problems with the PyGithub import
from github import Github

from django.conf import settings

from ..models import Issue, Status


def sync_to_github():
    issues = Issue.objects.filter(status_id=2, issue_tracker_id=None)
    for issue in issues:
        print('Adding to Github "{0}"'.format(issue.title))
        github_issue = add_issue_to_github(issue)
        issue.issue_tracker_id = github_issue.number
        issue.save()


def add_issue_to_github(issue):
    github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
    github_repo = github.get_repo(settings.ISSUES_REPO)
    label = github_get_label(github_repo, settings.ISSUES_LABEL)
    return github_repo.create_issue(issue.title, issue.body, labels=[label])


def github_get_label(github_repo, label_text):
    """
    Return a github issue object for supplied label_text
    """
    labels = github_repo.get_labels()
    #labels = github_repo.get_labels(name='CMS') # Not supported, add patch
    for label in labels:
        if label.name == label_text:
            return label
    return False


def sync_from_github():
    """
    Close accepted issues which are closed on Github.
    This is be done by closing any issues which aren't returned as being open
    PyGithub only returns open issues and we just want to hit the API once per
    call
    """
    # TODO: move this to model to simplify code
    accepted_issue_ids = set(
        Issue.objects.filter(status_id=2, issue_tracker_id__isnull=False)
        .values_list('issue_tracker_id', flat=True))
    open_issue_ids = set()

    for github_issue in github_get_all_issues():
        if github_issue.number in accepted_issue_ids:
            open_issue_ids.add(github_issue.number)

    closed_issue_ids = accepted_issue_ids - open_issue_ids
    closed_status = Status.objects.get(pk=4)
    Issue.objects.filter(issue_tracker_id__in=closed_issue_ids) \
        .update(status=closed_status);
    print('accepted_issue_ids', accepted_issue_ids)
    print('open_issue_ids', open_issue_ids)
    print('clossed_issue_ids', closed_issue_ids)


def github_get_all_issues():
    """
    Get all Github issues, note this only returns open issues
    """
    github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
    github_repo = github.get_repo(settings.ISSUES_REPO)
    return github_repo.get_issues()
    # Returns github.PaginatedList.PaginatedList of github.Issue.Issue
    # Do we need extra code to handle pagination?
