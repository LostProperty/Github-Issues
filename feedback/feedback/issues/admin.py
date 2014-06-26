from django.contrib import admin

from .models import Issue, Status


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'issue_tracker_id')
    list_filter = ['status', 'issue_tracker_id']
    search_fields = ['title']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
