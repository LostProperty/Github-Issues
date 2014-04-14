# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table(u'issues_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'issues', ['Status'])

        # Adding field 'Issue.created_at'
        db.add_column(u'issues_issue', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 14, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Issue.updated_at'
        db.add_column(u'issues_issue', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 4, 14, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Issue.status'
        db.add_column(u'issues_issue', 'status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['issues.Status']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table(u'issues_status')

        # Deleting field 'Issue.created_at'
        db.delete_column(u'issues_issue', 'created_at')

        # Deleting field 'Issue.updated_at'
        db.delete_column(u'issues_issue', 'updated_at')

        # Deleting field 'Issue.status'
        db.delete_column(u'issues_issue', 'status_id')


    models = {
        u'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['issues.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'issues.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['issues']
