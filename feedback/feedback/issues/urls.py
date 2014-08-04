from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from .views import (list_issues, add_issue, edit_issue, logout_view,
    issue_details)


urlpatterns = patterns(
    '',
    url(r'^$', list_issues, name='list_issues'),
    url(r'^issue/(?P<issue_id>\d+)$', issue_details,
        name='issue_details'),
    url(r'^issue/edit/(?P<issue_id>\d+)$', edit_issue,
        name='edit_issue'),
    url(r'^add', add_issue, name='add_issue'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout_view, name='logout')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        #     'document_root': settings.STATIC_ROOT,
        # }),
)
