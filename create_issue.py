import os

from github import Github


repo = 'LostProperty/dove-ath'
filter_label_text =  'Feedback'
token = os.getenv('FEEDBACK_GITHUB_TOKEN')

g = Github(token)
github_repo = g.get_repo(repo)
issue = github_repo.create_issue('Test issue', labels=False) # milestone=False
print(issue.number)
