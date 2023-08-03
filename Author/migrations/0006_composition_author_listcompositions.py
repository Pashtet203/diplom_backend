# Generated by Django 4.2 on 2023-05-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0005_alter_author_img_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('song_path', models.FileField(upload_to='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='author',
            name='listCompositions',
            field=models.ManyToManyField(to='Author.composition'),
        ),
    ]
