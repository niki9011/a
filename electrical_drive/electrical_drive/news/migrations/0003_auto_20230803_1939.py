# Generated by Django 3.1.4 on 2023-08-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230803_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allnews',
            old_name='category',
            new_name='subject',
        ),
    ]
