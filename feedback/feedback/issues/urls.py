from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib.auth.views import login
from django.views.generic import TemplateView

from .views import (list_issues, add_issue, edit_issue, logout_view)
from .mvp_views import list_repos, list_orgs, export_issues


urlpatterns = patterns(
    '',
    url(r'^repos$', list_repos, name='list_repos'),
    url(r'^$', list_orgs, name='list_orgs'),
    url(r'^export$', export_issues, name='export'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^about$', TemplateView.as_view(template_name='mvp/about.html')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
