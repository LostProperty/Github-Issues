import requests
#from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


def get_access_token(request):
    social_auth = request.user.social_auth.get()
    return social_auth.extra_data['access_token']


def call_github_api(url, request):
    response = requests.get('https://api.github.com{}'.format(url),
        params={'access_token': get_access_token(request)})
    return response.json()


@login_required
def list_repos(request):
    """
    List a users repos
    """
    org = request.GET.get('org')
    if org is None:
        url = '/user/repos'
    else:
        url = '/orgs/{}/repos'.format(org)
    repos = call_github_api(url, request)
    # TODO: sort repos alphabetically
    return TemplateResponse(request, 'mvp/repos.html',
        {'repos': repos, 'org': org})


@login_required
def list_orgs(request):
    """
    Lists a users organisation
    """
    response = requests.get('https://api.github.com/user/orgs',
        params={'access_token': get_access_token(request)})
    orgs = response.json()
    return TemplateResponse(request, 'mvp/orgs.html', {'orgs': orgs})


@login_required
def export_issues(request):
    """
    Export the users issues as Excel
    """
    # TODO: create an excel file
    # TODO: force the excel download for the user
    # TODO: get the issues from the API, add them to the excel file
    return TemplateResponse(request, 'mvp/orgs.html', {})
