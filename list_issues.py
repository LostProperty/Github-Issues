import sys

from github import Github
from github_utils import get_label
from settings import repo, filter_label_text, token


github = Github(token)
github_repo = github.get_repo(repo)

# Is it possible to filter by labels without having to call get labels first?
# Dig in the code to see what is required to create the label object
filter_label = get_label(github_repo, filter_label_text)
if filter_label == False:
    sys.exit('Error: Could not find label "{0}"'.format(filter_label_text))

issues = github_repo.get_issues(labels=[filter_label])
for issue in issues:
    # TODO: check if getting assignee is causing another network request
    # try:
    #     assignee = issue.assignee.name
    # except:
    #     assignee = 'Not assigned'
    # issue.labels, assignee))
    print('#{0} {1}'.format(issue.number, issue.title))
