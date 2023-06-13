# Generated by Django 4.2.2 on 2023-06-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
