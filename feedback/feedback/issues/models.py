from django.db import models

from django_extensions.db.fields import (CreationDateTimeField,
                                          ModificationDateTimeField)


class TimeStampedModel(models.Model):
    created_at = CreationDateTimeField()
    updated_at = ModificationDateTimeField()

    class Meta:
        abstract = True


class IssueManager(models.Manager):
    def get_accepted_issues(self):
        """
        Get accepted issues with Github issues
        """
        return self.filter(status_id=2, issue_tracker_id__isnull=False)


class Issue(TimeStampedModel):
    title = models.CharField(max_length=140)
    developer_title = models.CharField(max_length=140, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    developer_body = models.TextField(null=True, blank=True)
    issue_tracker_id = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey('Status')
    objects = IssueManager()

    @property
    def number(self):
        return self.pk

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('status', 'created_at')


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Status'
        ordering = ('pk',)
