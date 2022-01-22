# Generated by Django 4.0 on 2022-01-22 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_alter_shopuser_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='tags')),
                ('about_me', models.TextField(verbose_name='About Me')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('W', 'Женский')], default='M', max_length=1, verbose_name='Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authapp.shopuser')),
            ],
        ),
    ]