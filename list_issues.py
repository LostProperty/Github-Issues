import os
from github import Github


repo = 'LostProperty/dove-ath'
filter_label_text =  'CMS'
token = os.getenv('FEEDBACK_GITHUB_TOKEN')

g = Github(token)
github_repo = g.get_repo(repo)
labels = github_repo.get_labels()
#labels = github_repo.get_labels(name='CMS') # Not supported, add a patch

for label in labels:
    if label.name == filter_label_text:
        filter_label = label

# Is it possible to filter by labels without having to call get labels first?
# Dig in the code to see what is required to create the label object
issues = github_repo.get_issues(labels=[filter_label])
for issue in issues:
    # TODO: check if getting assignee is causing another network request
    # try:
    #     assignee = issue.assignee.name
    # except:
    #     assignee = 'Not assigned'
    # issue.labels, assignee))
    print('#{0} {1}'.format(issue.number, issue.title))
