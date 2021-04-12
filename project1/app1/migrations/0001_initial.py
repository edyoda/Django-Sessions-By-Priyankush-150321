# Generated by Django 3.1.7 on 2021-03-17 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descripton', models.CharField(blank=True, max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
