# Generated by Django 4.1 on 2023-08-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_alter_question_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='notes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='second_answer',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]