# Generated by Django 4.2.1 on 2023-05-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_answer_options_question_correct_way_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('upload', models.ImageField(upload_to='image/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
