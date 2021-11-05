# Generated by Django 3.2.9 on 2021-11-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
    ]
