# Generated by Django 3.0 on 2023-05-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_diff',
            field=models.FloatField(null=True),
        ),
    ]
