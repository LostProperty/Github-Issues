import pytest

#from django.http import Http404
from django.contrib.auth.models import AnonymousUser #,User

from issues.views import list_issues, add_issue


@pytest.mark.django_db
def test_list_issues_requires_logged_in_user(request_with_session):
    request_with_session.user = AnonymousUser()
    response = list_issues(request_with_session)
    assert response.status_code == 302
    assert response._headers['location'] == ('Location', '/login?next=/slash_doesnt_matter')


@pytest.mark.django_db
def test_add_issue_requires_staff_user(request_with_session):
    request_with_session.user = AnonymousUser()
    response = add_issue(request_with_session)
    assert response.status_code == 302
    assert response._headers['location'] == ('Location', '/login?next=/slash_doesnt_matter')


# TODO: test_list_issues_returns_multiple_issues (mock github object?)
# TODO: test_adding_an_issue_increments_total_issues (mock github object?)
