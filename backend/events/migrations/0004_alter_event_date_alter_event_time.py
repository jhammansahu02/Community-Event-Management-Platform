# Generated by Django 5.1.3 on 2024-11-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
