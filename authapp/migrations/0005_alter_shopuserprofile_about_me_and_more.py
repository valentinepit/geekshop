# Generated by Django 4.0 on 2022-01-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_shopuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuserprofile',
            name='about_me',
            field=models.TextField(verbose_name='Обо мне'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('W', 'Женский')], default='M', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='tagline',
            field=models.CharField(blank=True, max_length=128, verbose_name='Тэги'),
        ),
    ]
