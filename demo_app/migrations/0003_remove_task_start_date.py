# Generated by Django 4.2.14 on 2024-08-02 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_rename_post_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
    ]
