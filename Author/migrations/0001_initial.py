# Generated by Django 4.2 on 2023-05-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('years_of_life', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
