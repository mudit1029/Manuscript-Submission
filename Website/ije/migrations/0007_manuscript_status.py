# Generated by Django 3.2.2 on 2021-07-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ije', '0006_manuscript_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='status',
            field=models.CharField(choices=[('S', 'SUBMITTED'), ('I', 'IN PROCESSING'), ('L', 'SUCCESSFUL '), ('F', 'FAILED')], default='S', max_length=1),
        ),
    ]