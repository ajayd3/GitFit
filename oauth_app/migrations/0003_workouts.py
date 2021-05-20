# Generated by Django 3.1.7 on 2021-04-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0002_userprofile_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_type', models.CharField(max_length=100)),
                ('workout_difficulty', models.CharField(max_length=100)),
                ('workout_info', models.CharField(max_length=1000)),
            ],
        ),
    ]
