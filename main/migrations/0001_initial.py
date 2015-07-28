# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import main.usermodels
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.EmailField(verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=254)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.', blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', main.usermodels.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Название', max_length=200)),
                ('statement', models.FileField(verbose_name='Условие', upload_to='')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('KID', models.CharField(verbose_name='ID', blank=True, max_length=10)),
                ('state', models.CharField(verbose_name='Конкурсное состояние', choices=[('OPENED', 'Конкурс открыт'), ('CLOSED', 'Конкурс закрыт')], max_length=10)),
                ('end_date', models.DateField(verbose_name='Дата окончания конкурса', null=True, blank=True)),
                ('student_num', models.PositiveIntegerField(default=0, verbose_name='Число студентов, решивших задачу')),
                ('rating', models.DecimalField(default=Decimal('Infinity'), verbose_name='Рейтинг', max_digits=9, decimal_places=8)),
                ('solution', models.FileField(verbose_name='Решение', blank=True, null=True, upload_to='')),
                ('comment', models.FileField(verbose_name='Комментарий', blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lastname', models.CharField(verbose_name='Фамилия', blank=True, max_length=50)),
                ('firstname', models.CharField(verbose_name='Имя', blank=True, max_length=50)),
                ('group', models.CharField(verbose_name='Группа', blank=True, max_length=6)),
                ('KID', models.CharField(default=0, verbose_name='ID', blank=True, max_length=10)),
                ('rating', models.DecimalField(default=Decimal('0.0'), verbose_name='Рейтинг', max_digits=11, decimal_places=8)),
                ('is_allowed', models.BooleanField(default=False, verbose_name='Допуск')),
                ('nec_conditions', models.BooleanField(default=False, verbose_name='Необходимые условия')),
                ('recommendation', models.BooleanField(default=False, verbose_name='Рекомендация преподавателя')),
                ('PRS', models.PositiveIntegerField(default=0, verbose_name='БРС')),
                ('test_mark', models.PositiveIntegerField(default=0, verbose_name='Семестровая')),
                ('solved_problems', models.ManyToManyField(to='main.Problem', blank=True)),
            ],
        ),
    ]
