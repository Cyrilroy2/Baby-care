# Generated by Django 5.0.4 on 2024-06-15 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritionists',
            name='age',
        ),
    ]
