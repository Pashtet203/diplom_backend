# Generated by Django 4.2 on 2023-05-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognize_song', '0003_alter_recognize_song_data_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize_song',
            name='data_song',
            field=models.FileField(upload_to=''),
        ),
    ]
