from django.db import models
from django.contrib.auth.models import User

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
    body = models.TextField(null=True, blank=True)
    issue_tracker_id = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey('Status')
    priority = models.ForeignKey(to='Priority', default=1)
    attachment = models.FileField(upload_to='attachments', blank=True,
        null=True)
    reported_by = models.ForeignKey(User)
    objects = IssueManager()

    @property
    def number(self):
        return self.pk

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('status', '-priority', '-created_at')


class Priority(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Priority'


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Status'
        ordering = ('pk',)


def get_next_or_prev(models, item, direction):
    '''
    Returns the next or previous item of
    a query-set for 'item'.

    'models' is a query-set containing all
    items of which 'item' is a part of.

    direction is 'next' or 'prev'

    '''
    getit = False
    if direction == 'prev':
        models = models.reverse()
    for m in models:
        if getit:
            return m
        if item == m:
            getit = True
    # if getit:
    #     # This would happen when the last
    #     # item made getit True
    #     return models[0]
    return False
