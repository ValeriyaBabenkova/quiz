# Generated by Django 5.1.4 on 2025-03-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_questions_num_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='num_question',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Номер вопроса'),
        ),
    ]
