# Generated by Django 4.2.2 on 2023-06-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_alter_job_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
