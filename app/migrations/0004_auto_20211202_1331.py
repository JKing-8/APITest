# Generated by Django 3.2.6 on 2021-12-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_dbproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='dblinkall',
            name='info',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='dblinkall',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
