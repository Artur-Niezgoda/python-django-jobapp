# Generated by Django 5.0 on 2024-01-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobpost_date_jobpost_description_jobpost_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
