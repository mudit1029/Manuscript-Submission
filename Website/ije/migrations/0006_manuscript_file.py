# Generated by Django 3.2.2 on 2021-07-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ije', '0005_auto_20210701_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='file',
            field=models.URLField(default='www.google.com'),
        ),
    ]
