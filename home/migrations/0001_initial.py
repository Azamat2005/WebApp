# Generated by Django 4.1.4 on 2023-07-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ism', models.CharField(max_length=60)),
                ('Familya', models.CharField(max_length=60)),
                ('Telefon', models.CharField(max_length=30)),
                ('Fan', models.CharField(max_length=30)),
            ],
        ),
    ]
