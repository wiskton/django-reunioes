# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reuniao'
        db.create_table('reunioes_reuniao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assunto', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('reunioes', ['Reuniao'])

        # Adding M2M table for field emails on 'Reuniao'
        db.create_table('reunioes_reuniao_emails', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reuniao', models.ForeignKey(orm['reunioes.reuniao'], null=False)),
            ('email', models.ForeignKey(orm['emails.email'], null=False))
        ))
        db.create_unique('reunioes_reuniao_emails', ['reuniao_id', 'email_id'])


    def backwards(self, orm):
        # Deleting model 'Reuniao'
        db.delete_table('reunioes_reuniao')

        # Removing M2M table for field emails on 'Reuniao'
        db.delete_table('reunioes_reuniao_emails')


    models = {
        'emails.email': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Email'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'reunioes.reuniao': {
            'Meta': {'ordering': "('assunto',)", 'object_name': 'Reuniao'},
            'assunto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emails.Email']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reunioes']