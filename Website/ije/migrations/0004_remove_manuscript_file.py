# Generated by Django 3.2.2 on 2021-06-30 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ije', '0003_manuscript_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manuscript',
            name='file',
        ),
    ]
