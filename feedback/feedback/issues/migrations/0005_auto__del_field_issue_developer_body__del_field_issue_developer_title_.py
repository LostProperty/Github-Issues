# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Issue.developer_body'
        db.delete_column(u'issues_issue', 'developer_body')

        # Deleting field 'Issue.developer_title'
        db.delete_column(u'issues_issue', 'developer_title')


        # Changing field 'Issue.created_at'
        db.alter_column(u'issues_issue', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Issue.updated_at'
        db.alter_column(u'issues_issue', 'updated_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Adding field 'Issue.developer_body'
        db.add_column(u'issues_issue', 'developer_body',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Issue.developer_title'
        db.add_column(u'issues_issue', 'developer_title',
                      self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Issue.created_at'
        db.alter_column(u'issues_issue', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Issue.updated_at'
        db.alter_column(u'issues_issue', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        u'issues.issue': {
            'Meta': {'ordering': "('status', 'created_at')", 'object_name': 'Issue'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_tracker_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['issues.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'issues.status': {
            'Meta': {'ordering': "('pk',)", 'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['issues']