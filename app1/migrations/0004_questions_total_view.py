# Generated by Django 2.1.5 on 2019-04-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20190316_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='total_view',
            field=models.IntegerField(default=0),
        ),
    ]
