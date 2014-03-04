import pytest

from django.contrib.auth.models import User
from django.contrib.sessions.backends.base import SessionBase


@pytest.fixture
def staff_user(commit=True):
    user = User(is_staff=True)
    if commit:
        user.save()
    return user


@pytest.fixture
def request_with_session(rf):
    request = rf.get('/slash_doesnt_matter')
    request.session = SessionBase()
    return request
