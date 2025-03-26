# Generated by Django 5.1.4 on 2025-03-25 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_questionnum_num_question_alter_tours_num_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='num_tour',
        ),
        migrations.AlterField(
            model_name='questions',
            name='num_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionnum', verbose_name='Номер вопроса'),
        ),
    ]
