# Generated by Django 5.0.3 on 2025-02-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
