# Generated by Django 2.1 on 2020-05-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField(unique=True)),
                ('short_slug', models.SlugField(default=None, max_length=64, unique=True)),
                ('salt', models.CharField(default=None, max_length=10)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
