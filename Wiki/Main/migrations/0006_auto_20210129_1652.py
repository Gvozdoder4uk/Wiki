# Generated by Django 3.1.5 on 2021-01-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=models.TextField(blank=True, help_text='ФИО пользователя', max_length=500), verbose_name='Фото пользователя'),
        ),
    ]
