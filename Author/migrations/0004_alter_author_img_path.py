# Generated by Django 4.2 on 2023-05-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0003_alter_author_img_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='img_path',
            field=models.TextField(default=''),
        ),
    ]