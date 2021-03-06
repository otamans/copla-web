# Generated by Django 2.0.6 on 2018-06-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='point_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
