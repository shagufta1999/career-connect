# Generated by Django 4.1.7 on 2023-04-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_jobapplicationform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplicationform',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]