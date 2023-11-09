# Generated by Django 4.2.6 on 2023-10-17 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Sarlavhasi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm')),
                ('content', models.TextField(verbose_name='Yangilik haqida')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sana')),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
    ]