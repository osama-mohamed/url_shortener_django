# Generated by Django 4.2.6 on 2023-10-31 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analytics',
            name='clicks',
        ),
    ]