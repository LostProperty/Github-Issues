from uuid import uuid1
import requests
import xlsxwriter

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.http import HttpResponse


def get_access_token(request):
    social_auth = request.user.social_auth.get()
    print(social_auth.extra_data['access_token'])
    return social_auth.extra_data['access_token']


def get_github_issues(org, repo, request, state=False):
    url = '/repos/{}/{}/issues'.format(org, repo)
    # ?per_page=100 # max number of issues you can get per page
    if state:
        url += '?state={}'.format(state)
    return call_github_api(url, get_access_token(request))


def call_github_api(url, access_token):
    response = requests.get('https://api.github.com{}'.format(url),
        params={'access_token': access_token})
    return response.json()


def create_excel(open_issues, closed_issues):
    filepath = '/tmp/{}.xlsx'.format(uuid1())
    workbook = xlsxwriter.Workbook(filepath)
    header_format = workbook.add_format({'bold': True})
    open_worksheet = workbook.add_worksheet('Open')
    closed_worksheet = workbook.add_worksheet('Closed')
    excel_add_issues(open_worksheet, open_issues, header_format)
    excel_add_issues(closed_worksheet, closed_issues, header_format)
    return filepath


def excel_add_issues(worksheet, issues, header_format):
    worksheet.set_column(1, 1, 60)
    worksheet.write(0, 0, 'Number', header_format)
    worksheet.write(0, 1, 'Title', header_format)
    worksheet.write(0, 2, 'Status', header_format)
    row = 1
    for issue in issues:
        worksheet.write(row, 0, issue['number'])
        worksheet.write(row, 1, issue['title'])
        worksheet.write(row, 2, issue['state'])
        row += 1


@login_required
def list_orgs(request):
    """
    Lists a users organisation
    """
    orgs = call_github_api('/user/orgs', get_access_token(request))
    orgs = sorted(orgs, key=lambda k: k['login'])
    return TemplateResponse(request, 'mvp/orgs.html', {'orgs': orgs})


@login_required
def list_repos(request):
    """
    List a users repos
    """
    org = request.GET.get('org')
    if org is None:
        org = request.user.username
        url = '/user/repos'
    else:
        url = '/orgs/{}/repos'.format(org)
    repos = call_github_api(url, get_access_token(request))
    repos = sorted(repos, key=lambda k: k['name'])
    return TemplateResponse(request, 'mvp/repos.html',
        {'repos': repos, 'org': org})


@login_required
def export_issues(request):
    """
    Export the users issues as Excel
    """
    # TODO: pass into function with nice URL routing
    repo = request.GET.get('repo')
    org = request.GET.get('org')
    open_issues = get_github_issues(org, repo, request)
    closed_issues = get_github_issues(org, repo, request, 'closed')
    filepath = create_excel(open_issues, closed_issues)
    # TODO: can we avoid writing the file and keep in memory?
    with open (filepath, 'r') as excel_file:
        data = excel_file.read()
    response = HttpResponse(data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(repo)
    return response
