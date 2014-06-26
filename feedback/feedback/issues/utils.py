from github import Github

from django.conf import settings

#name = 'x'
#issues_backend = __import__('.db_issues', fromlist=['db_issues'], name = 'x')
#issues_backend = getattr(__import__('.db_issues'), 'db_issues')
#from .github_utils import github_get_label


import imp

issues_backend = imp.new_module('./xdb_issues')
# from issues_backend import get_issues

def get_issues(filter_label):
    issues_backend.db_get_issues()

def get_label():
    pass

def get_issue():
    pass

#def get_issues(filter_label):

# TODO:
# - how to use an abstract base class in Python? (Java stule interface)
# - how to import for a file name (module) given in settings (so dynamic)
# - dummy backend
# - json file backend
# - DB backend

# def get_label():
#     # TODO: can we do something more elegant here instead of else if
#     if settings.ISSUES_BACKEND == 'dummy':
#         return settings.ISSUES_LABEL
#     elif settings.ISSUES_BACKEND == 'github':
#         # TODO: move to git_utils? Or extend class?
#         # Auth users has a much higher API limit than the token
#         # TODO: investigate Oauth2 key/secret http://developer.github.com/v3/#authentication
#         github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
#         github_repo = github.get_repo(settings.ISSUES_REPO)
#         return github_get_label(github_repo, settings.ISSUES_LABEL)


# def get_issues(filter_label):
#     if settings.ISSUES_BACKEND == 'dummy':
#         # TODO: get this from file
#         return [
#             {
#                 'number': 1,
#                 'title': 'Make me a sandwich',
#                 'date': 'Tue 26th March',
#                 'status': 'new'
#             },
#             {
#                 'number': 2,
#                 'title': 'Make the logo bigger',
#                 'date': 'Tue 26th March',
#                 'status': 'open'
#             },
#             {
#                 'number': 3,
#                 'title': 'Needs more pop',
#                 'date': 'Tue 26th March',
#                 'status': 'to dicuss'
#             },
#             {
#                 'number': 4,
#                 'title': 'Getting a web error',
#                 'date': 'Tue 26th March',
#                 'status': 'to dicuss'
#             },
#             {
#                 'number': 5,
#                 'title': 'Title is mandatory',
#                 'date': 'Tue 26th March',
#                 'status': 'done'
#             },
#             {
#                 'number': 5,
#                 'title': 'Dragon should be green',
#                 'date': 'Tue 26th March',
#                 'status': 'done'
#             }
#         ]

#     elif settings.ISSUES_BACKEND == 'github':
#         github = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)
#         github_repo = github.get_repo(settings.ISSUES_REPO)
#         return github_repo.get_issues(labels=[filter_label])


# def get_issue(issue_id):
#     if settings.ISSUES_BACKEND == 'dummy':
#         return {
#             'number': 4,
#             'title': 'Getting a web error',
#             'description': 'When I go to http://google.co.uk/ I see the message "Unable to connect to the Internet" and a drawing of a Dinosaur above it.',
#             'reported_by': 'Pete',
#             'date': 'Tue 26th March'
#         }
#     elif settings.ISSUES_BACKEND == 'github':
#         pass
