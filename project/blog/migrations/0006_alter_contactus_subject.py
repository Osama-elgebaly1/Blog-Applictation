# Generated by Django 5.0.3 on 2025-02-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contactus_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=500),
        ),
    ]
