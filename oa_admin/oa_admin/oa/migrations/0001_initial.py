# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'oa_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'oa', ['Department'])

        # Adding model 'Position'
        db.create_table(u'oa_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'oa', ['Position'])

        # Adding model 'Role'
        db.create_table(u'oa_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'oa', ['Role'])

        # Adding model 'User'
        db.create_table(u'oa_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('real_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('gender', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pre_year_holiday', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('remain_year_holiday', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('superior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.User'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Position'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Role'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.Department'])),
        ))
        db.send_create_signal(u'oa', ['User'])

        # Adding model 'Leave'
        db.create_table(u'oa_leave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.User'])),
            ('leave_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('reason_for_leave', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('leave_time_begin', self.gf('django.db.models.fields.DateTimeField')()),
            ('leave_time_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('verify_status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'oa', ['Leave'])

        # Adding model 'Attendance'
        db.create_table(u'oa_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oa.User'])),
            ('punchwork', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('punchworkoff', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'oa', ['Attendance'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'oa_department')

        # Deleting model 'Position'
        db.delete_table(u'oa_position')

        # Deleting model 'Role'
        db.delete_table(u'oa_role')

        # Deleting model 'User'
        db.delete_table(u'oa_user')

        # Deleting model 'Leave'
        db.delete_table(u'oa_leave')

        # Deleting model 'Attendance'
        db.delete_table(u'oa_attendance')


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
            'superior': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oa.User']"}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['oa']