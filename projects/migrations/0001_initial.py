# Generated by Django 3.1 on 2020-08-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(max_length=64)),
                ('goal', models.CharField(max_length=64)),
                ('satisfaction_rate', models.IntegerField()),
            ],
        ),
    ]
