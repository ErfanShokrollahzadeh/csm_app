# Generated by Django 5.0.1 on 2024-01-14 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
