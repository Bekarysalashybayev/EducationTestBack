# Generated by Django 4.2.1 on 2023-05-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('NIS', 'NIS')], max_length=10, unique=True, verbose_name='Тип Теста')),
                ('duration', models.IntegerField(verbose_name='Длительность в минутах')),
            ],
            options={
                'verbose_name': 'Тип теста',
                'verbose_name_plural': 'Тип теста',
                'db_table': 'test_type',
            },
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='order',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='test_type',
        ),
        migrations.AlterField(
            model_name='variant',
            name='test_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_type_variants', to='quiz.testtype', verbose_name='Тип Теста'),
        ),
        migrations.CreateModel(
            name='TestTypeLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Очередь')),
                ('duration', models.IntegerField(verbose_name='Длительность в минутах')),
                ('has_by_lesson', models.BooleanField(default=False, verbose_name='По очереди')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_type_lessons', to='quiz.lesson', verbose_name='Предмет')),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_types', to='quiz.testtype', verbose_name='Тип Теста')),
            ],
            options={
                'verbose_name': 'Предметы теста',
                'verbose_name_plural': 'Предметы теста',
                'db_table': 'test_type_lesson',
                'unique_together': {('test_type', 'lesson')},
            },
        ),
    ]
