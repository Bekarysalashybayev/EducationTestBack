# Generated by Django 4.2.1 on 2023-05-26 12:45

import core.constants.AnswerChoices
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_answer_choice_alter_testtype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.CharField(choices=[('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], default=core.constants.AnswerChoices.ANSWER_CHOICES['CHOICE'], max_length=12, verbose_name='Тип Ответа'),
        ),
    ]
