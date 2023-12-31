# Generated by Django 4.2.7 on 2023-11-14 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('Front-end разработка', 'Front-end разработка'), ('Back-end разработка', 'Back-end разработка'), ('Мобильная разработка', 'Мобильная разработка'), ('Data science', 'Data science'), ('UX/UI дизайн', 'UX/UI дизайн')], max_length=45)),
                ('sex', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=1)),
                ('city_of_residence', models.CharField(max_length=15, verbose_name='Город проживания')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('citizenship', models.CharField(max_length=20)),
                ('profile_photo', models.ImageField(blank=True, height_field=472, upload_to='profile', width_field=354)),
                ('skills', models.TextField(verbose_name='Навыки, скиллы')),
                ('cover_letter', models.TextField(verbose_name='Сопроводительное письмо')),
                ('education', models.CharField(choices=[('Среднее', 'Среднее'), ('Среднее специальное', 'Среднее специальное'), ('Неоконченное высшее', 'Неоконченное высшее'), ('Высшее', 'Высшее'), ('Бакалавр', 'Бакалавр'), ('Магистр', 'Магистр'), ('Кандидат наук', 'Кандидат наук'), ('Доктор наук', 'Доктор наук')], max_length=20, verbose_name='Уровень образования')),
                ('expected_salary', models.CharField(blank=True, max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
