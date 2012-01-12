# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'ZipCode', fields ['longitude']
        db.create_index('django_geo_zipcode', ['longitude'])

        # Adding index on 'ZipCode', fields ['latitude']
        db.create_index('django_geo_zipcode', ['latitude'])

        # Adding index on 'ZipCode', fields ['zip_code']
        db.create_index('django_geo_zipcode', ['zip_code'])


    def backwards(self, orm):
        
        # Removing index on 'ZipCode', fields ['zip_code']
        db.delete_index('django_geo_zipcode', ['zip_code'])

        # Removing index on 'ZipCode', fields ['latitude']
        db.delete_index('django_geo_zipcode', ['latitude'])

        # Removing index on 'ZipCode', fields ['longitude']
        db.delete_index('django_geo_zipcode', ['longitude'])


    models = {
        'django_geo.zipcode': {
            'Meta': {'object_name': 'ZipCode'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'})
        }
    }

    complete_apps = ['django_geo']
