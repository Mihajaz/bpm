# Generated by Django 2.2.16 on 2025-03-11 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdm_app', '0004_auto_20250311_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='Total_hosting',
            new_name='total_hosting',
        ),
    ]
