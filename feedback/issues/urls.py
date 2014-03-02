from django.conf.urls import patterns, url
from .views import list_issues, add_issue


urlpatterns = patterns(
    '',
    url(r'^$', list_issues, name='list_issues'),
    url(r'^add', add_issue, name='add_issue'),
)
