# Generated by Django 3.1.7 on 2021-03-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210317_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]