# Generated by Django 4.2.3 on 2023-07-31 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='content',
            new_name='contents',
        ),
    ]
