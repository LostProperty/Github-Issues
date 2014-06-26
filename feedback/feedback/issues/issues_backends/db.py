from ..models import Issue


def get_label():
    pass


def get_issues(filter_label):
    # TODO: do processing/formatting on issues before returning
    return Issue.objects.all()


def get_issue(issue_id):
    pass


def add_issue(title, body):
    pass
