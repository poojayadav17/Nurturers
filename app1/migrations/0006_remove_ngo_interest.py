# Generated by Django 2.1.5 on 2019-04-23 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_upcomingevents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='interest',
        ),
    ]
