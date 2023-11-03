# Generated by Django 4.2.6 on 2023-11-02 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_url_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='short_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_data', to='shortener.url'),
        ),
    ]