# Generated by Django 5.1.4 on 2025-03-25 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_tours_alter_answers_answer_right_alter_answers_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'Номер тура', 'verbose_name_plural': 'Номера туров'},
        ),
        migrations.AlterField(
            model_name='tours',
            name='num_tour',
            field=models.IntegerField(verbose_name='Номер тура'),
        ),
        migrations.CreateModel(
            name='QuestionNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_question', models.IntegerField(verbose_name='Номер вопроса')),
                ('num_tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tours', verbose_name='Номер тура')),
            ],
            options={
                'verbose_name': 'Номер вопроса',
                'verbose_name_plural': 'Номера вопросов',
            },
        ),
    ]
