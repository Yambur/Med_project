# Generated by Django 4.2 on 2024-05-29 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('text', models.TextField(verbose_name='текст')),
                ('date', models.DateTimeField(verbose_name='дата и время отзыва')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/', verbose_name='Иконка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'специализация',
                'verbose_name_plural': 'специализации',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person/', verbose_name='Фото')),
                ('speciality', models.ManyToManyField(related_name='speciality', to='med.speciality', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'врач',
                'verbose_name_plural': 'врачи',
            },
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('price', models.PositiveIntegerField(verbose_name='стоимость')),
                ('doctor', models.ManyToManyField(related_name='врач', to='med.doctor')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='услуги', to='med.speciality', verbose_name='специализация')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='дата и время приема')),
                ('diagnostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='записи', to='med.diagnostic', verbose_name='диагностика')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='записи', to='med.doctor', verbose_name='врач')),
            ],
            options={
                'verbose_name': 'запись на диагностику',
                'verbose_name_plural': 'записи на диагностику',
            },
        ),
    ]
