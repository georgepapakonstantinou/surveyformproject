# Generated by Django 4.1 on 2023-10-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0015_alter_question_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=750),
        ),
    ]
