import requests
import xlsxwriter

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.http import HttpResponse


def get_access_token(request):
    social_auth = request.user.social_auth.get()
    print(social_auth.extra_data['access_token'])
    return social_auth.extra_data['access_token']


def get_github_issues(org, repo, request):
    url = '/repos/{}/{}/issues'.format(org, repo)
    return call_github_api(url, get_access_token(request))


def call_github_api(url, access_token):
    response = requests.get('https://api.github.com{}'.format(url),
        params={'access_token': access_token})
    return response.json()


def create_excel(issues):
    # TODO: should we create this in /tmp? use uuid for filename
    filepath = 'issues.xlsx'
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Number')
    worksheet.write(0, 1, 'Title')
    worksheet.write(0, 2, 'Status')

    row = 1
    for issue in issues:
        worksheet.write(row, 0, issue['number'])
        worksheet.write(row, 1, issue['title'])
        worksheet.write(row, 2, issue['state'])
        row += 1
    # TODO: larger field for title
    # TODO: split sheets for open and closed
    return filepath


@login_required
def list_orgs(request):
    """
    Lists a users organisation
    """
    orgs = call_github_api('/user/orgs', get_access_token(request))
    orgs = sorted(orgs, key=lambda k: k['login'])
    # TODO: pass the repos_url to the list_repos view
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
    issues = get_github_issues(org, repo, request)
    filepath = create_excel(issues)
    # TODO: can we avoid writing the file and keep in memory?
    with open (filepath, 'r') as excel_file:
        data = excel_file.read()
    response = HttpResponse(data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="issues.xls"'
    return response


 #    {u'assignee': {u'avatar_url': u'https://avatars.githubusercontent.com/u/84706?v=3',
 #               u'events_url': u'https://api.github.com/users/rob-b/events{/privacy}',
 #               u'followers_url': u'https://api.github.com/users/rob-b/followers',
 #               u'following_url': u'https://api.github.com/users/rob-b/following{/other_user}',
 #               u'gists_url': u'https://api.github.com/users/rob-b/gists{/gist_id}',
 #               u'gravatar_id': u'',
 #               u'html_url': u'https://github.com/rob-b',
 #               u'id': 84706,
 #               u'login': u'rob-b',
 #               u'organizations_url': u'https://api.github.com/users/rob-b/orgs',
 #               u'received_events_url': u'https://api.github.com/users/rob-b/received_events',
 #               u'repos_url': u'https://api.github.com/users/rob-b/repos',
 #               u'site_admin': False,
 #               u'starred_url': u'https://api.github.com/users/rob-b/starred{/owner}{/repo}',
 #               u'subscriptions_url': u'https://api.github.com/users/rob-b/subscriptions',
 #               u'type': u'User',
 #               u'url': u'https://api.github.com/users/rob-b'},
 # u'body': u'When restarting nginx on ATH production servers you see the following error:\r\n```\r\n$ sudo service nginx restart\r\nRestarting nginx: nginx: [warn] conflicting server name "unilever.rzf.lostpropertyhq.com" on 0.0.0.0:80, ignored\r\nnginx: [warn] conflicting server name "p1.unilever.rzf.lostpropertyhq.com" on 0.0.0.0:80, ignored\r\nnginx.\r\n````\r\nRob said provisioning the servers will remove the warning.',
 # u'closed_at': None,
 # u'comments': 0,
 # u'comments_url': u'https://api.github.com/repos/LostProperty/dove-ath/issues/640/comments',
 # u'created_at': u'2015-03-12T15:11:36Z',
 # u'events_url': u'https://api.github.com/repos/LostProperty/dove-ath/issues/640/events',
 # u'html_url': u'https://github.com/LostProperty/dove-ath/issues/640',
 # u'id': 60834233,
 # u'labels': [],
 # u'labels_url': u'https://api.github.com/repos/LostProperty/dove-ath/issues/640/labels{/name}',
 # u'locked': False,
 # u'milestone': None,
 # u'number': 640,
 # u'state': u'open',
 # u'title': u'Nginx warning on ATH production',
 # u'updated_at': u'2015-03-12T15:11:56Z',
 # u'url': u'https://api.github.com/repos/LostProperty/dove-ath/issues/640',
 # u'user': {u'avatar_url': u'https://avatars.githubusercontent.com/u/245475?v=3',
 #           u'events_url': u'https://api.github.com/users/pxg/events{/privacy}',
 #           u'followers_url': u'https://api.github.com/users/pxg/followers',
 #           u'following_url': u'https://api.github.com/users/pxg/following{/other_user}',
 #           u'gists_url': u'https://api.github.com/users/pxg/gists{/gist_id}',
 #           u'gravatar_id': u'',
 #           u'html_url': u'https://github.com/pxg',
 #           u'id': 245475,
 #           u'login': u'pxg',
 #           u'organizations_url': u'https://api.github.com/users/pxg/orgs',
 #           u'received_events_url': u'https://api.github.com/users/pxg/received_events',
 #           u'repos_url': u'https://api.github.com/users/pxg/repos',
 #           u'site_admin': False,
 #           u'starred_url': u'https://api.github.com/users/pxg/starred{/owner}{/repo}',
 #           u'subscriptions_url': u'https://api.github.com/users/pxg/subscriptions',
 #           u'type': u'User',
 #           u'url': u'https://api.github.com/users/pxg'}}
