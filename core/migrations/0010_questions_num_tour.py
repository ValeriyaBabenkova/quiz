# Generated by Django 5.1.4 on 2025-03-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_gameslist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='num_tour',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Номер тура'),
        ),
    ]
