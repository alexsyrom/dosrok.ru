# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators
import main.usermodels
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.EmailField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=254, unique=True, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', blank=True, verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', blank=True, verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', main.usermodels.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('statement', models.FileField(upload_to='', verbose_name='Условие')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('KID', models.CharField(editable=False, max_length=10, verbose_name='ID')),
                ('state', models.CharField(choices=[('OPENED', 'Конкурс открыт'), ('CLOSED', 'Конкурс закрыт')], max_length=10, verbose_name='Конкурсное состояние')),
                ('end_date', models.DateField(blank=True, verbose_name='Дата окончания конкурса', null=True)),
                ('student_num', models.PositiveIntegerField(editable=False, default=0, verbose_name='Число студентов, решивших задачу')),
                ('rating', models.DecimalField(editable=False, max_digits=9, default=Decimal('0.0'), decimal_places=8, verbose_name='Рейтинг')),
                ('solution', models.FileField(blank=True, verbose_name='Решение', upload_to='', null=True)),
                ('comment', models.FileField(blank=True, verbose_name='Комментарий', upload_to='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lastname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('firstname', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('group', models.CharField(blank=True, max_length=6, verbose_name='Группа')),
                ('KID', models.CharField(editable=False, blank=True, max_length=10, unique=True, verbose_name='ID')),
                ('rating', models.DecimalField(editable=False, max_digits=11, default=Decimal('0.0'), decimal_places=8, verbose_name='Рейтинг')),
                ('is_allowed', models.BooleanField(default=False, verbose_name='Допуск')),
                ('nec_conditions', models.BooleanField(default=False, verbose_name='Необходимые условия')),
                ('recommendation', models.BooleanField(default=False, verbose_name='Рекомендация преподавателя')),
                ('PRS', models.PositiveIntegerField(default=0, verbose_name='БРС')),
                ('test_mark', models.PositiveIntegerField(default=0, verbose_name='Семестровая')),
                ('solved_problems', models.ManyToManyField(blank=True, to='main.Problem')),
            ],
        ),
    ]
