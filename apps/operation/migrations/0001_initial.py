# Generated by Django 2.0.4 on 2018-04-08 15:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('mobile', models.CharField(max_length=11, verbose_name='mobile')),
                ('course', models.CharField(max_length=50, verbose_name='course_name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'user_ask',
                'verbose_name_plural': 'user_ask',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'user_course',
                'verbose_name_plural': 'user_course',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='data_id')),
                ('fav_type', models.IntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '讲师')], default=1, verbose_name='favorite_type')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'user_favorite',
                'verbose_name_plural': 'user_favorite',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='receive_user')),
                ('message', models.CharField(max_length=500, verbose_name='msg_content')),
                ('has_read', models.BooleanField(default=False, verbose_name='has_read_msg')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'user_msg',
                'verbose_name_plural': 'user_msg',
            },
        ),
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('usercourse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='operation.UserCourse')),
                ('comments', models.CharField(max_length=200, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'course_comments',
                'verbose_name_plural': 'course_comments',
            },
            bases=('operation.usercourse',),
        ),
    ]
