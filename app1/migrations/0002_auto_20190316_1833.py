# Generated by Django 2.1.5 on 2019-03-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='interest',
            name='imageurl',
            field=models.URLField(blank=True, null=True),
        ),
    ]