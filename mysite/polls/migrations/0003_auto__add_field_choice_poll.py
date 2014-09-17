# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Choice.poll'
        db.add_column(u'polls_choice', 'poll',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['polls.Poll']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Choice.poll'
        db.delete_column(u'polls_choice', 'poll_id')


    models = {
        u'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"})
        },
        u'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['polls']