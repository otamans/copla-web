# Generated by Django 2.0.6 on 2018-06-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180617_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('fr', 'Без продвижения'), ('att', 'С продвижением'), ('adv', 'Рекламный')], default='fr', max_length=10, unique=True),
        ),
    ]
