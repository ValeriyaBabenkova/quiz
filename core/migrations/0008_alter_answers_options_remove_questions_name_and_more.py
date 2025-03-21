# Generated by Django 5.1.4 on 2025-02-15 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_questions_options_rename_games_questions_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Проверка ответов', 'verbose_name_plural': 'Проверка ответов'},
        ),
        migrations.RemoveField(
            model_name='questions',
            name='name',
        ),
        migrations.AddField(
            model_name='questions',
            name='name_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.gameslist', verbose_name='Название игры'),
        ),
    ]
