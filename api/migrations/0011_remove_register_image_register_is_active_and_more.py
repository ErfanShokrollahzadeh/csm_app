# Generated by Django 5.0.1 on 2024-02-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='image',
        ),
        migrations.AddField(
            model_name='register',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='register',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
