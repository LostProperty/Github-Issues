import random

from github import Github

from github_utils import get_label
from settings import repo, filter_label_text, token


g = Github(token)
github_repo = g.get_repo(repo)
issue_title = 'Test issue {0}'.format(random.randint(0, 100))
label = get_label(github_repo, filter_label_text)
issue = github_repo.create_issue(issue_title, labels=[label])  # milestone=False
print(issue.number)
