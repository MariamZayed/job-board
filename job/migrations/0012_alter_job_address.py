# Generated by Django 4.2.2 on 2023-06-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_job_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
