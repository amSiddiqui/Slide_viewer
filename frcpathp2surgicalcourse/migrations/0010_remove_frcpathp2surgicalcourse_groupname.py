# Generated by Django 3.0.8 on 2021-01-18 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frcpathp2surgicalcourse', '0009_frcpathp2surgicalcourse_groupname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frcpathp2surgicalcourse',
            name='GroupName',
        ),
    ]