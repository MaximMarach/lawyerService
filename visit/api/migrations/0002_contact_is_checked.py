# Generated by Django 4.1.7 on 2023-03-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name='Прошел ли консультацию?'),
        ),
    ]
