# Generated by Django 4.1.7 on 2023-03-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('second_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия пользователя')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Почта')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')),
                ('description', models.TextField(verbose_name='Описание проблемы')),
                ('date_of_call', models.DateField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'request',
                'ordering': ['date_of_call'],
            },
        ),
    ]