# Generated by Django 3.1.7 on 2021-04-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=20)),
                ('marks', models.IntegerField(default=35)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
