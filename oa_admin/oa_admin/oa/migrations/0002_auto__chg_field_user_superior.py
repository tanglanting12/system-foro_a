# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.superior'
        db.alter_column(u'oa_user', 'superior_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.User'], null=True))

    def backwards(self, orm):

        # Changing field 'User.superior'
        db.alter_column(u'oa_user', 'superior_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['oa.User']))

    models = {
        u'oa.attendance': {
            'Meta': {'object_name': 'Attendance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punchwork': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'punchworkoff': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.User']"})
        },
        u'oa.department': {
            'Meta': {'object_name': 'Department'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'oa.leave': {
            'Meta': {'object_name': 'Leave'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leave_time_begin': ('django.db.models.fields.DateTimeField', [], {}),
            'leave_time_end': ('django.db.models.fields.DateTimeField', [], {}),
            'leave_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reason_for_leave': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.User']"}),
            'verify_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'oa.position': {
            'Meta': {'object_name': 'Position'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'oa.role': {
            'Meta': {'object_name': 'Role'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'oa.user': {
            'Meta': {'object_name': 'User'},
            'birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Department']"}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Position']"}),
            'pre_year_holiday': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'real_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'remain_year_holiday': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.Role']"}),
            'superior': ('django.db.models.fields.related.ForeignKey', [], {'default': "'null'", 'to': u"orm['oa.User']", 'null': 'True', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['oa']