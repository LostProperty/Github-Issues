# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Issue.attachment'
        db.add_column(u'issues_issue', 'attachment',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Issue.attachment'
        db.delete_column(u'issues_issue', 'attachment')


    models = {
        u'issues.issue': {
            'Meta': {'ordering': "('status', '-priority', '-created_at')", 'object_name': 'Issue'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_tracker_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['issues.Priority']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['issues.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'issues.priority': {
            'Meta': {'object_name': 'Priority'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'issues.status': {
            'Meta': {'ordering': "('pk',)", 'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['issues']