# Generated by Django 4.2.5 on 2023-09-29 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('''
                INSERT INTO store_collection (title)
                VALUES ('collection1')
    ''', '''
                DELETE INTO store_collection
                WHERE title='collection1'          
    '''
    )
    ]

