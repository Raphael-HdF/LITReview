# Generated by Django 4.0.4 on 2022-06-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_managers_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=2048, verbose_name='User description'),
        ),
    ]
