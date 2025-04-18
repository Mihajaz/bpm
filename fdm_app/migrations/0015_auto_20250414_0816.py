# Generated by Django 2.2.16 on 2025-04-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdm_app', '0014_auto_20250409_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='hosting_days',
            field=models.IntegerField(default=1, help_text='nombre de jours de sejour'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='meal_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='prix des repas', max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='shipping_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='frais de transport', max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='various_expenses_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='prix des divers frais', max_digits=10),
        ),
    ]
