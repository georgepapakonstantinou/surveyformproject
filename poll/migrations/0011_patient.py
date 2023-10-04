# Generated by Django 4.1 on 2023-08-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0010_alter_choice_notes_alter_choice_second_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EDUCCATEGORY', models.CharField(max_length=100, null=True)),
                ('EDUCPATIENT', models.CharField(max_length=100, null=True)),
                ('SEXPATIENT', models.CharField(max_length=100, null=True)),
                ('AGEPATIENT', models.CharField(max_length=10, null=True)),
                ('ECUCCARERCAT', models.CharField(max_length=100, null=True)),
                ('EDUCCARER', models.CharField(max_length=100, null=True)),
                ('SEXCARER', models.CharField(max_length=100, null=True)),
                ('AGECARER', models.CharField(max_length=100, null=True)),
                ('RELATIONSHIPCARER', models.CharField(max_length=100, null=True)),
                ('LIVESIN', models.CharField(max_length=100, null=True)),
                ('kentro', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('NPI', models.CharField(max_length=100, null=True)),
                ('STAGE', models.CharField(max_length=100, null=True)),
                ('IADL', models.CharField(max_length=100, null=True)),
                ('MMSE', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]