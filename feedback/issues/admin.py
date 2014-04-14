from django.contrib import admin

from .models import Issue, Status


admin.site.register(Issue)
admin.site.register(Status)
