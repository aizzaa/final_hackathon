# Generated by Django 4.2.7 on 2023-11-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resume_applied_vacancies'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='status',
            field=models.CharField(blank=True, choices=[('viewed', 'Просмотрено'), ('rejected', 'Отказано'), ('contact_soon', 'Кандидатура подходит, скоро свяжемся')], max_length=20, null=True),
        ),
    ]
