# Generated by Django 3.1.7 on 2021-03-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
