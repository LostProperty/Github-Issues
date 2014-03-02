import random

from github import Github

from github_utils import get_label, get_milestone
from settings import repo, filter_label_text, token, milestone_title


g = Github(token)
github_repo = g.get_repo(repo)
issue_title = 'Test issue {0}'.format(random.randint(0, 100))
label = get_label(github_repo, filter_label_text)
milestone = get_milestone(github_repo, milestone_title)

issue = github_repo.create_issue(issue_title, labels=[label],
    milestone=milestone)
print(issue.number)
