# Generated by Django 5.1.4 on 2025-03-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_tours_options_alter_tours_num_tour_questionnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnum',
            name='num_question',
            field=models.CharField(max_length=100, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='num_tour',
            field=models.CharField(max_length=100, verbose_name='Номер тура'),
        ),
    ]
