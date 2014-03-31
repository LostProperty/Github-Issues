from github import Github

from django.conf import settings

from .github_utils import github_get_label


def get_label():
    # TODO: can we do something more elegant here instead of else if
    if settings.ISSUES_BACKEND == 'dummy':
        return settings.ISSUES_LABEL
    elif settings.ISSUES_BACKEND == 'github':
        # TODO: move to git_utils? Or extend class?
        # Auth users has a much higher API limit than the token
        # TODO: investigate Oauth2 key/secret http://developer.github.com/v3/#authentication
        github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
        github_repo = github.get_repo(settings.ISSUES_REPO)
        return github_get_label(github_repo, settings.ISSUES_LABEL)

def get_issues(filter_label):
    if settings.ISSUES_BACKEND == 'dummy':
        # TODO: get this from file
        return [
            {
                'number': 1,
                'title': 'Make me a sandwich'
            },
            {
                'number': 2,
                'title': 'Make the logo bigger'
            }
        ]

    elif settings.ISSUES_BACKEND == 'github':
        github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
        github_repo = github.get_repo(settings.ISSUES_REPO)
        return github_repo.get_issues(labels=[filter_label])
