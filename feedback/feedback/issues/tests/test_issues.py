import pytest

from django.contrib.auth.models import AnonymousUser,User
from django.contrib.sessions.backends.base import SessionBase

from ..views import list_issues, add_issue, edit_issue, issue_details
from ..forms import IssueForm
from ..models import Issue


def test_list_issues_requires_logged_in_user(request_with_session):
    request_with_session.user = AnonymousUser()
    response = list_issues(request_with_session)
    assert response.status_code == 302
    assert response._headers['location'] == ('Location', '/login?next=/slash_doesnt_matter')


def test_add_issue_requires_logged_in_user(request_with_session):
    request_with_session.user = AnonymousUser()
    response = add_issue(request_with_session)
    assert response.status_code == 302
    assert response._headers['location'] == ('Location', '/login?next=/slash_doesnt_matter')


@pytest.mark.django_db
def test_list_issues_returns_an_issue(request_with_session, new_issue):
    request_with_session.user = User()
    response = list_issues(request_with_session)
    assert response.status_code == 200
    assert len(response.context_data['issues']) == 1
    assert response.context_data['issues'][0].title == 'Test title'


def test_add_issue_status_code_200(request_with_session):
    request_with_session.user = User()
    response = add_issue(request_with_session)
    assert response.status_code == 200


@pytest.mark.django_db
def test_issue_details_status_code_200(request_with_session, new_issue):
    request_with_session.user = User()
    response = issue_details(request_with_session, new_issue.id)
    assert response.status_code == 200


def test_issue_form_fields_required(request_with_session):
    form = IssueForm()
    assert form.fields['title'].required
    assert form.fields['priority'].required


@pytest.mark.django_db
def test_edit_issue_status_code_200(request_with_session, new_issue):
    request_with_session.user = User()
    response = edit_issue(request_with_session, new_issue.id)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_issue_post_success(rf):
    data = {
        'title': 'make the logo bigger',
        'priority': 2
    }
    request = rf.post('/slash_doesnt_matter', data=data)
    request.session = SessionBase()
    request.user = User()
    response = add_issue(request)

    assert response.status_code == 302 # redirects on creation
    new_issue = Issue.objects.all()[0]
    assert new_issue.title == 'make the logo bigger'
    assert new_issue.priority.name == 'normal'
    assert new_issue.status.name == 'New'


@pytest.mark.django_db
def test_edit_issue_post_success(rf, new_issue):
    data = {
        'title': 'make the logo even BIGGER!',
        'priority': 2
    }
    request = rf.post('/slash_doesnt_matter', data=data)
    request.session = SessionBase()
    request.user = User()
    response = edit_issue(request, new_issue.id)

    assert response.status_code == 302 # redirects on creation
    new_issue = Issue.objects.all()[0]
    assert new_issue.title == 'make the logo even BIGGER!'
    assert new_issue.priority.name == 'normal'
    assert new_issue.status.name == 'New'


@pytest.mark.django_db
def test_staff_user_has_process_issue_controls(request_with_session, new_issue):
    request_with_session.user = User(is_staff=True)
    response = issue_details(request_with_session, new_issue.id)
    response.render()
    assert response.status_code == 200
    assert '<input type="submit" value="Accept"' in response._container[0]
    assert '<input type="submit" value="Needs Dicussion"' in response._container[0]
