# Note can't call this file github.py as that causes problems with the PyGithub import
from github import Github

from django.conf import settings

from ..models import Issue


def sync_to_github():
    issues = Issue.objects.filter(status_id=2, issue_tracker_id=None)
    for issue in issues:
        print(issue)
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
