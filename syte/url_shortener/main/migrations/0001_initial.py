# Generated by Django 3.1.2 on 2021-07-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('longLink', models.TextField()),
                ('hash', models.TextField()),
                ('clicks', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('linkId', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
