# Generated by Django 2.0.1 on 2023-10-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0009_auto_20231005_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactlist',
            name='dateexpired',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='contactlist',
            name='datejoined',
            field=models.DateField(null=True),
        ),
    ]
