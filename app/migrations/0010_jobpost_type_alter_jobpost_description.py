# Generated by Django 5.0 on 2024-01-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobpost_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='Full Time', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]