# Generated by Django 3.1.2 on 2020-10-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
