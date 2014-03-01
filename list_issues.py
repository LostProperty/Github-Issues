import os
from github import Github

repo = 'LostProperty/dove-ath'
label = 'cms' #'feedback'
token = os.getenv('FEEDBACK_GITHUB_TOKEN')

g = Github(token)
github_repo = g.get_repo(repo)
# TODO: filter on tag here
issues = github_repo.get_issues()

for issue in issues:
    # TODO: check if getting assignee is causing another network request
    # try:
    #     assignee = issue.assignee.name
    # except:
    #     assignee = 'Not assigned'
    # issue.labels, assignee))
    print('#{0} {1}'.format(issue.number, issue.title))
